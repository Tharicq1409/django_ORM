from django.db import models
from django.contrib.auth.models import User  #used to import default user model
# Create your models here.

#model to store Retaurant related data
class Restaurant(models.Model):
    class RestaurantType(models.TextChoices):
        INDIAN = 'IN','Indian'
        CHINESE = 'CH','Chinese'
        ITALIAN = 'IT','Italian'
        OTHERS = 'OT','Others'
        
    name = models.CharField(max_length=50)
    website = models.CharField(default=' ')
    date_opened = models.DateField()
    restaurant_type = models.CharField(max_length=2,choices=RestaurantType.choices,default='IN')
    latitude =  models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        return self.name

#model to store Rating from the user
class Rating(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE) #Foreign Key from User Model
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE) #Foreign Key from Restaurant
    rating = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return f"Rating:{self.rating}"
    

class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.SET_NULL,null=True)
    
