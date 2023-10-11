from django.contrib.auth.models import User
from ORMapp.models import Restaurant,Rating
from django.utils import timezone
from django.db import connection
def run():
    '''
    #Adding data to Restaurant table.
    restaurant = Restaurant()
    restaurant.name = 'Italian Restaurant'
    restaurant.latitude = 50.2
    restaurant.longitude = 50.2
    restaurant.date_opened = timezone.now()
    restaurant.restaurant_type = Restaurant.RestaurantType.ITALIAN
    
    restaurant.save()
    
    #restaurant = Restaurant.objects.all()
    #restaurant = Restaurant.objects.first() #fetch first row
    restaurant = Restaurant.objects.all()[0] #Indexing
    print(restaurant)
    #print(connection.queries)
    
    Restaurant.objects.create(
        name="Pizza Hub",
        latitude = 50.2,
        longitude = 50.2,
        date_opened = timezone.now(),
        restaurant_type = Restaurant.RestaurantType.ITALIAN
        
    )
    #restaurant = Restaurant.objects.count() #prints count of records
    restaurant = Restaurant.objects.all()
    print(restaurant)
    
    restaurant_name = Restaurant.objects.first()
    user_name = User.objects.first()
    #Rating.objects.create(user_name=user_name,restaurant=restaurant_name,rating=3)
    restaurant_rating = Rating.objects.filter(rating=3) #filtering based on Condition 
    print(restaurant_rating)
    print(connection.queries)'''
    
    #updating Existing record
    restaurant = Restaurant.objects.first()
    
    restaurant.name = 'Italiant Multi Crusine Rstaurant'
    restaurant.save()
    
    print(restaurant)