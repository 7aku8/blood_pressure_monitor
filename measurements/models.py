from django.db import models

from your_health.models import UserData


class Measurement(models.Model):
    userdata = models.ForeignKey(UserData, on_delete=models.PROTECT)

    measurement_time = models.DateTimeField(auto_now_add=True, editable=False)

    systolic_pressure = models.SmallIntegerField(null=False, blank=False, default=120, verbose_name='Ciśnienie skurczowe')
    diastolic_pressure = models.SmallIntegerField(null=False, blank=False, default=80, verbose_name='Ciśnienie rozkurczowe')
    pulse = models.SmallIntegerField(null=False, blank=False, default=60, verbose_name='Tętno')

    class Meta:
        ordering = ['-measurement_time']

    def __str__(self):
        info_message = 'Pomiar dla: {user}, wynik: {systolic}/{diastolic}, tętno: {pulse}'.format(
            user=userdata.get_full_name(),
            systolic=self.systolic_pressure,
            diastolic=self.diastolic_pressure,
            pulse=self.pulse
        )
    