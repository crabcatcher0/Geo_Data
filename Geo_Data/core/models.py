from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=100)
    longitutude = models.FloatField(null=False, default=0, blank=False)
    latitude = models.FloatField(null=False, blank=False, default=0)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=100)
    in_city = models.ForeignKey("City", on_delete=models.CASCADE)  # type: ignore
    longitude = models.FloatField(default=0, null=False, blank=False)
    latitude = models.FloatField(default=0, null=False, blank=False)

    def __str__(self):
        return self.hospital_name


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField()
    available_status = models.BooleanField(default=False)
    lost_status = models.BooleanField(default=False)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    total_amount = models.FloatField()
