from django.db import models

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=100, blank=False)
    role = models.CharField(max_length=20, blank=False)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.role})"


class Diner(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=200, unique=True, blank=True)
    phone_num = models.CharField(max_length=20, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name