from django.db import models
from orders.models import Order

# Create your models here.
class Feedback(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    rating = models.IntegerField()  # e.g. 1-5
    comment = models.TextField(blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback (Order #{self.order.pk}): {self.rating}"
