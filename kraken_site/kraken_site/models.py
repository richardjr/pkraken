from django.conf import settings
from django.db import models

# model for user settings
class UserSettings(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # kraken api keys and features
    api_key = models.CharField(max_length=100, blank=True, null=True)
    elec_mpan = models.CharField(max_length=100, blank=True, null=True)
    elec_serial = models.CharField(max_length=100, blank=True, null=True)
    gas_mprn = models.CharField(max_length=100, blank=True, null=True)
    gas_serial = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.user.username