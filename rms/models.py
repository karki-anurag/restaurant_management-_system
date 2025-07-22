from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    Items_name = models.CharField(max_length=100)
    Items_price = models.FloatField( null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')

    def __str__(self):
        return self.Items_name

class Tables(models.Model):
    table_number = models.IntegerField(unique=True)
    is_available = models.BooleanField(default=True)
    table_size = models.IntegerField(null = False, blank=False)

    def __str__(self):
        return self.table_number

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Tables, on_delete=models.CASCADE, blank=True, null=True)
    payment_status = models.BooleanField(default=False)

    def __self__(self):
        return f"Order {self.user.username} - {'Paid' if self.payment_status else 'Pending'}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    menu_item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price_at_order = models.FloatField()

    def __str__(self):
        return f"{self.menu_item.Items_name} - {self.quantity}"
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Storage(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='storages')
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.ingredient.name} - {self.quantity} {self.unit}"

class Recipe(models.Model):
    menu_item = models.OneToOneField(MenuItems, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')