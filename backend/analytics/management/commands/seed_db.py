# filepath: /home/baku/Coding/restaurant_management_app/backend/orders/management/commands/seed_db.py
from django.core.management.base import BaseCommand
from accounts.models import Staff, Diner
from menu.models import Menu, MenuItem
from orders.models import Order, OrderItem, Payment
from reviews.models import Feedback

class Command(BaseCommand):
    help = 'Seeds the database with initial data if it is empty'

    def handle(self, *args, **kwargs):
        if not Staff.objects.exists() or not Diner.objects.exists() or not Menu.objects.exists() or not MenuItem.objects.exists() or not Order.objects.exists() or not OrderItem.objects.exists() or not Payment.objects.exists() or not Feedback.objects.exists():
            self.stdout.write(self.style.SUCCESS('Seeding database...'))
            
            # Add your seeding logic here
            # Example seeding for Staff
            staff = Staff.objects.create(name="John Doe", role="Manager")
            
            # Example seeding for Diner
            diner = Diner.objects.create(name="Jane Doe", email="jane@example.com", phone_num="1234567890")
            
            # Example seeding for Menu and MenuItem
            menu = Menu.objects.create(name="Fast Food Menu", description="Our fast food menu, tasty bro", image="menu_images/fast-food-menu.jpg")
            menu_item = MenuItem.objects.create(name="Burger", description="Delicious burger", price=9.99, menu=menu, image="menu_item_images/burger.jpg")
            
            # Example seeding for Order and OrderItem
            order = Order.objects.create(service_type="Dine-In", diner=diner)
            order_item = OrderItem.objects.create(order=order, menu_item=menu_item, quantity=2)
            
            # Example seeding for Payment
            payment = Payment.objects.create(order=order, method="CASH")
            
            # Example seeding for Feedback
            feedback = Feedback.objects.create(order=order, rating=5, comment="Great service!")
            
            self.stdout.write(self.style.SUCCESS('Database seeded successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('Database already has data. Skipping seeding...'))