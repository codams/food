from .models import Food, Day
from ariadne import convert_kwargs_to_snake_case
from django.http import HttpResponseBadRequest, Http404

@convert_kwargs_to_snake_case
def list_foods(*_):
    return [
        {"name": food.name, "days": food.days.all(), "color": food.color, "id":food.id}
        for food in Food.objects.all()
    ]
    
@convert_kwargs_to_snake_case
def list_days(*_):
    return [
        {"date": day.date}
        for day in Day.objects.all()
    ]

@convert_kwargs_to_snake_case
def create_food(*_, name, color):
    food = Food.objects.create(name=name, color=color)
    return {"name": food.name}

@convert_kwargs_to_snake_case
def get_food(*_, name=None, id=None):
    if not id and not name:
        return HttpResponseBadRequest("Id or name needed")
    food = None
    if id:
        food = Food.objects.get(id=id)
        
    if name and not food:
        food = Food.objects.get(name=name)
        
    if not food:
        return Http404('Not found')
    
    return {"name": food.name, "days": food.days.all()}

@convert_kwargs_to_snake_case
def create_day(*_, date):
    day = Day.objects.create(date=date)
    return {"date": day.date}

@convert_kwargs_to_snake_case
def update_food_date(*_, id, date):
    if not id:
        return HttpResponseBadRequest("Id needed")
    food = Food.objects.get(id=id)
    if not food:
        return Http404("Food not found")
    
    day, created = Day.objects.get_or_create(date=date)
    
    food.days.add(day.id)
    food.save()
    return food

    
    
    
