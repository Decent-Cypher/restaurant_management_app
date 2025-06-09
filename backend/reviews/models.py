from django.db import models
from django.utils import timezone
from orders.models import Order

# Create your models here.
class Feedback(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField()  # e.g. 1-5
    comment = models.TextField(blank=True)
    time_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Feedback (Order #{self.order.pk if self.order else None}): {self.rating}"
