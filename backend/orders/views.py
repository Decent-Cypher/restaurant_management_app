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

def submit_order(request) -> JsonResponse:
    """
    Submit the order for processing
    """
    if request.method == "POST":
        diner_id = request.POST.get("diner_id")
        service_type = request.POST.get("service_type", "Dine-in") #default to Dine-in
        note = request.POST.get("note", "")
        address = request.POST.get("address", "") # Optional, for delivery orders
        ordered_items = request.POST.getlist("ordered_items")  # expecting list of item IDs
        quantities = request.POST.getlist("quantities")        # matching list of quantities
        time_created = request.POST.get("time_created", timezone.now())
        last_modified = request.POST.get("last_modified", timezone.now())

        # Validate diner
        try:
            diner = Diner.objects.get(id=diner_id)
        except Diner.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Diner not found"})

        # Create the new order (status defaults to 'PENDING')
        new_order = Order.objects.create(
            diner=diner,
            service_type=service_type,
            note=note
        )

        # Add order items
        total_price = 0
        for item_id, qty in zip(ordered_items, quantities):
            try:
                menu_item = MenuItem.objects.get(id=item_id)
            except MenuItem.DoesNotExist:
                continue
            OrderItem.objects.create(
                order=new_order,
                menu_item=menu_item,
                quantity=int(qty)
            )
            total_price += menu_item.price * int(qty)
        new_order.total_price = total_price
        new_order.save()

        return JsonResponse({
            "status": "success",
            "order_id": new_order.id,
            "order_status": new_order.status
        })
    return JsonResponse({
        "status": "error",
        "message": "Invalid request method"
    })

def update_order(request) -> JsonResponse:
    """
    Update the order details
    """
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        updated_items = request.POST.getlist("ordered_items")  # expecting list of item IDs
        updated_quantities = request.POST.getlist("quantities")  # matching list of quantities
        updated_note = request.POST.get("note", "")

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})

        # Update order items
        total_price = 0
        order.orderitem_set.all().delete()  # Clear existing items
        for item_id, qty in zip(updated_items, updated_quantities):
            try:
                menu_item = MenuItem.objects.get(id=item_id)
            except MenuItem.DoesNotExist:
                continue
            OrderItem.objects.create(
                order=order,
                menu_item=menu_item,
                quantity=int(qty)
            )
            total_price += menu_item.price * int(qty)

        # Update note and total price
        order.notes = updated_note
        order.total_price = total_price
        order.last_modified = timezone.now()
        order.save()

        return JsonResponse({"status": "success", "message": "Order updated successfully"})

    return JsonResponse({"status": "error", "message": "Invalid request method"})

def get_order_status(request) -> JsonResponse:
    """
    Get the status of a specific order
    """
    if request.method == "POST":
        order_id = request.POST.get("order_id")

        try:
            order = Order.objects.get(id=order_id)
            return JsonResponse({
                "status": "success",
                "order_status": order.status,
                "total_price": order.total_price, # Return the total price too
                "last_modified": order.last_modified.strftime("%Y-%m-%d %H:%M:%S")
            })
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})

    return JsonResponse({"status": "error", "message": "Invalid request method"})

def pay_order(request) -> JsonResponse:
    """
    Process payment for an order
    """
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        payment_method = request.POST.get("payment_method")

        try:
            order = Order.objects.get(id=order_id)
            if order.status != 'PENDING': 
                return JsonResponse({"status": "error", "message": "Order already processed"})

            # Create payment instance
            payment = Payment.objects.create(
                order=order,
                method=payment_method,
                status='paid'
            )
            order.status = 'COMPLETED'
            order.save()

            return JsonResponse({"status": "success", "payment_id": payment.id, "payment_status": payment.status})

        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})
        except Payment.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Payment not found"})

    return JsonResponse({"status": "error", "message": "Invalid request method"})
