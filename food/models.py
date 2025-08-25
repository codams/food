from django.db import models
from django.http import Http404
from datetime import datetime

# Create your models here.

class Day(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField("date")
    def __str__(self):
        return self.date.strftime("%B %d, %Y %I:%M %p")
    
class Food(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    days = models.ManyToManyField(Day, blank=True)
    
    def __str__(self):
        return self.name


def has_this_food_been_eaten(food_string):
    food, created = Food.objects.get_or_create(name=food_string)
    if created:
        return False
    if not food.days:
        return False
    return True

def when_has_this_food_been_eaten(food_string):
    food = Food.objects.get(name=food_string)
    return food.days.order_by('date').all()

def when_has_this_food_been_eaten_lastly(food_string):
    food = Food.objects.get(name=food_string)
    if not food:
        raise Http404('Food not found')
    return food.days.order_by('date').first()