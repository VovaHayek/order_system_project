from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='logo/', blank=True)
    
    def __str__(self):
        return self.name

class Food(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name_of_food = models.CharField(max_length=100)
    price = models.IntegerField(blank=False)
    dish_image = models.ImageField(upload_to='dishes/', blank=True)

    def __str__(self):
        return self.name_of_food

class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Food, blank=False)

    def __str__(self):
        return self.restaurant
