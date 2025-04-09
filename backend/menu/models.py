from django.db import models

# Create your models here.

class Menu(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=500, blank=False)
    image = models.ImageField(upload_to='menu_images/', blank=False, null=False)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
    image = models.ImageField(upload_to='menu_item_images/', blank=False, null=False)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.price}"