from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View

from libs.KrakenAPI import KrakenAPI
from .forms import LoginForm, UserSettingsForm
from .models import UserSettings


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dash/')
        else:
            form.add_error(None, 'Invalid username or password')
            return render(request, 'login.html', {'form': form})


class DashboardView(View):
    def get(self, request):
        userSettings = UserSettings.objects.get(user=request.user)
        form = UserSettingsForm(instance=userSettings)
        context = self.get_meter_overviews(userSettings)
        context['form'] = form
        return render(request, 'dash.html', context)

    def post(self, request):
        userSettings = UserSettings.objects.get(user=request.user)
        form = UserSettingsForm(request.POST, instance=userSettings)

        if form.is_valid():
            form.save()
            context = self.get_meter_overviews(userSettings)
            context['form'] = form
            return render(request, 'dash.html', context)

    def get_meter_overviews(self, userSettings):
        # get meter overviews from kraken api
        kraken = KrakenAPI(userSettings.api_key)
        mpan = kraken.get_meter_point(userSettings.elec_mpan)
        consumption = kraken.get_meter_point_consumption(userSettings.elec_mpan,userSettings.elec_serial)
        consumption_gas = kraken.get_gas_meter_point_consumption(userSettings.gas_mprn,userSettings.gas_serial)
        return {
            'mpan': mpan,
            'consumption':consumption,
            'consumption_gas': consumption_gas
        }

