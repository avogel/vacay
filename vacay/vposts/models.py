from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    contents = models.TextField()
    date_written = models.DateField()
    likes = models.ManyToManyField(User, related_name='likes')

    def __unicode__(self):
        return self.title



class Trip(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    is_completed = models.BooleanField()
    user = models.ForeignKey(User, related_name="trips")
    ideas = models.ManyToManyField(Post, related_name="trip_ideas")

    def __unicode__(self):
        return self.name + " for user " + self.user.username

class VisitedCity(models.Model):
    city_name = models.CharField(max_length=50)
    city_number = models.IntegerField()
    trip = models.ForeignKey(Trip, related_name="visited_cities")
    ideas = models.ManyToManyField(Post, related_name="city_ideas")

    def __unicode__(self):
        return self.city_name + " for trip " + self.trip.name

    class Meta:
        ordering = ['city_number', 'id']

class VisitedDay(models.Model):
    date = models.DateField(blank=True)
    day_number = models.IntegerField()
    visited_city = models.ForeignKey(VisitedCity, related_name='visited_days')
    written_posts = models.ManyToManyField(Post, related_name='written_posts')
    ideas = models.ManyToManyField(Post, related_name='ideas')

    def __unicode__(self):
        return str(self.date) + " for " + str(self.visited_city)

    class Meta:
        ordering = ['day_number', 'id']

class Tag(models.Model):
    name = models.CharField(max_length=50)
    tagged_posts = models.ManyToManyField(Post, related_name='tagged_posts')
    tagged_days = models.ManyToManyField(VisitedDay, related_name='tagged_days')
    tagged_cities = models.ManyToManyField(VisitedCity, related_name='tagged_cities')
    tagged_trips = models.ManyToManyField(Trip, related_name='tagged_trips')