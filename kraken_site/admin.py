# add UserSettings to the admin site
from django.contrib import admin
from .models import UserSettings



@admin.register(UserSettings)
class UserSettings(admin.ModelAdmin):
    list_display = ('api_key', 'elec_mpan', 'elec_serial', 'gas_mprn', 'gas_serial')