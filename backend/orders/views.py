from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Order, OrderItem, Payment
from menu.models import MenuItem
from accounts.models import Diner

@csrf_exempt
def add_order_item(request: HttpResponse) -> JsonResponse:
    """
    Add an item to a customer's order
    """
    # Protect view: only logged in diners allowed
    if "diner_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)

    if request.method == "POST":
        # Get the order ID and item details from the request
        order_id = request.POST.get("order_id")
        item_name = request.POST.get("item_name")
        item_quantity = request.POST.get("item_quantity")
        
        try:
            order = Order.objects.get(id=order_id)
            # Create a new OrderItem instance
            order_item = OrderItem(
                order=order,
                menu_item=item_name,  # Assuming item_name is used to fetch the MenuItem (adjust if necessary)
                quantity=item_quantity,
            )
            order_item.save()
            order.total_price += order_item.menu_item.price * int(item_quantity)
            order.last_modified = timezone.now()
            order.save()
            return JsonResponse({"status": "success", "item": order_item.id, "order": order.id})
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def remove_order_item(request: HttpResponse) -> JsonResponse:
    """
    Remove an item from a customer's order
    """
    # Protect view
    if "diner_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)
        
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        item_name = request.POST.get("item_name")
        quantity = request.POST.get("remove_quantity")
        
        try:
            quantity = int(quantity)
        except (TypeError, ValueError):
            return JsonResponse({"status": "error", "message": "Invalid quantity"})

        try: 
            order = Order.objects.get(id=order_id)
            try:
                # Assuming MenuItem has a 'name' field to filter by
                order_item = OrderItem.objects.get(menu_item__name=item_name, order=order)
                if order_item.quantity <= quantity:
                    order.total_price -= order_item.menu_item.price * order_item.quantity
                    order_item.delete()
                else:
                    order_item.quantity -= quantity
                    order.total_price -= order_item.menu_item.price * quantity
                    order_item.save()
                order.last_modified = timezone.now()
                order.save()
                return JsonResponse({"status": "success"})
            except OrderItem.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Item not found"})
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def add_note(request: HttpResponse) -> JsonResponse:
    """
    Add a note to a customer's order
    """
    # Protect view
    if "diner_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)
        
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        note = request.POST.get("note", "")
        try:
            order = Order.objects.get(id=order_id)
            order.note = note  # Using field 'note' on Order as defined in the model
            order.save()
            return JsonResponse({"status": "success"})
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def choose_service(request: HttpResponse) -> JsonResponse:
    """
    Select service options for the order
    """
    # Protect view
    if "diner_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)
        
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        service_options = request.POST.get("service_type", "Dine-in")  # default to Dine-in
        try:
            order = Order.objects.get(id=order_id)
            order.service_type = service_options
            order.save()
            return JsonResponse({"status": "success"})
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def submit_order(request) -> JsonResponse:
    """
    Submit the order for processing
    """
    # Protect view
    if "diner_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)
        
    if request.method == "POST":
        diner_id = request.POST.get("diner_id")
        service_type = request.POST.get("service_type", "Dine-in")  # default to Dine-in
        note = request.POST.get("note", "")
        address = request.POST.get("address", "")  # Optional, for delivery orders
        ordered_items = request.POST.getlist("ordered_items")  # expecting list of item IDs
        quantities = request.POST.getlist("quantities")         # matching list of quantities
        
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
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def update_order(request) -> JsonResponse:
    """
    Update the order details
    """
    # Protect view
    if "diner_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)
        
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        updated_items = request.POST.getlist("ordered_items")  # expecting list of item IDs
        updated_quantities = request.POST.getlist("quantities")  # matching list of quantities
        updated_note = request.POST.get("note", "")
        
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})
        
        # Clear existing items
        order.order_items.all().delete()
        total_price = 0
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
            
        order.note = updated_note
        order.total_price = total_price
        order.last_modified = timezone.now()
        order.save()
        
        return JsonResponse({"status": "success", "message": "Order updated successfully"})
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def get_order_status(request) -> JsonResponse:
    """
    Get the status of a specific order
    """
    # Protect view
    if "diner_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)
        
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        try:
            order = Order.objects.get(id=order_id)
            return JsonResponse({
                "status": "success",
                "order_status": order.status,
                "total_price": float(order.total_price),
                "last_modified": order.last_modified.strftime("%Y-%m-%d %H:%M:%S")
            })
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"})
    return JsonResponse({"status": "error", "message": "Invalid request method"})

@csrf_exempt
def pay_order(request) -> JsonResponse:
    """
    Process payment for an order
    """
    # Protect view
    if "staff_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)
        
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
    return JsonResponse({"status": "error", "message": "Invalid request method"})