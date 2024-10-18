from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=100)
    longitutude = models.FloatField(null=False, default=0, blank=False)
    latitude = models.FloatField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name
