from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dash')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})