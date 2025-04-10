from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Order, OrderItem
from django.utils import timezone

# Create your views here.
def add_order_item(request: HttpResponse) -> JsonResponse: # Frontend
    """
    Add an item to a customer's order
    """
    # TODO
    # 1. Modify the total price and the last modified time of the customer's order -> done
    # 2. In case of not found an order (e.g. The first time the customer orders), create a new order for the customer
    
    if request.method == "POST":
        # Get the order ID and item details from the request
        order_id = request.POST.get("order_id")
        item_name = request.POST.get("item_name")
        item_quantity = request.POST.get("item_quantity") 
        
        try:
            order = Order.objects.get(id=order_id)
            # Create a new OrderItem instance
            order_item = OrderItem(
                order=order_id,
                menu_item=item_name,
                quantity=item_quantity,
            )
            order_item.save()
            order.total_price += order_item.menu_item.price * item_quantity
            order.last_modified = timezone.now()
        except:
            return JsonResponse({"status": "error", "message": "Order not found"})

        # Return a success response
        return JsonResponse({"status": "success", "item": order_item, "order": order})

    return JsonResponse({"status": "error", "message": "Invalid request method"})

def remove_order_item(request: HttpResponse) -> JsonResponse:
    """
    Remove an item from a customer's order
    """
    # TODO
    # 1. Modify the total price and the last modified time of the customer's order
    # 2. How to select a specific order item with the item name to remove from database
    if request.method == "POST":
        # Get the order ID from the request
        order_id = request.POST.get("order_id")
        # Get the order item name and quantity from the request
        item_name = request.POST.get("item_name")
        quantity = request.POST.get("quantity")

        try: 
            order = Order.objects.get(id=order_id)
            # Delete the OrderItem instance
            try:     
                order_item = OrderItem.objects.get(item_name=item_name, order=order_id)
                if order_item.quantity <= quantity:
                    order_item.delete()
                    return JsonResponse({"status": "success", "message": "Remove item"})
                else:
                    order_item.quantity -= quantity
                order.total_price -= order_item.menu_item.price * quantity
                order.last_modified = timezone.now()
                order_item.save()
                order.save()
                return JsonResponse({"status": "success"})
            except OrderItem.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Item not found"})
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})

    return JsonResponse({"status": "error", "message": "Invalid request method"})

def add_note(request: HttpResponse) -> JsonResponse:
    """
    Add a note to a customer's order
    """
    if request.method == "POST":
        # Get the order ID and note from the request
        order_id = request.POST.get("order_id")
        note = request.POST.get("note")

        # Get the Order instance
        try:
            order = Order.objects.get(id=order_id)
            order.notes = note
            order.save()
            return JsonResponse({"status": "success"})
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})

    return JsonResponse({"status": "error", "message": "Invalid request method"})

def choose_service(request: HttpResponse) -> JsonResponse:
    """
    Select service options for the order
    """
    if request.method == "POST":
        # Get the order ID and service options from the request
        order_id = request.POST.get("order_id")
        service_options = request.POST.get("service_options")

        # Get the Order instance
        try:
            order = Order.objects.get(id=order_id)
            order.service_type = service_options
            order.save()
            return JsonResponse({"status": "success"})
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})