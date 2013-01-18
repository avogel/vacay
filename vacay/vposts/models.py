from django.db import models

class Account(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    current_city = models.CharField(max_length=50)
    about_me = models.CharField(max_length=1000)
    email = models.EmailField()


class Trip(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    account = models.ForeignKey(Account)

class VisitedCity(models.Model):
    city_name = models.CharField(max_length=50)
    trip = models.ForeignKey(Trip)

class VisitedDay(models.Model):
    date = models.DateField()
    visited_cities = models.ManyToManyField(VisitedCity)

class Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    visited_days = models.ManyToManyField(VisitedDay)