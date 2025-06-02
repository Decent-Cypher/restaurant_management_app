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
        item_id = request.POST.get("item_id")  # Changed from item_name to item_id
        item_quantity = request.POST.get("item_quantity")
        
        try:
            order = Order.objects.get(id=order_id)
            try:
                menu_item = MenuItem.objects.get(id=item_id)
            except MenuItem.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Menu item not found"}, status=404)
            # Create a new OrderItem instance
            order_item = OrderItem(
                order=order,
                menu_item=menu_item,
                quantity=item_quantity,
            )
            order_item.save()
            order.total_price += menu_item.price * int(item_quantity)
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
        item_id = request.POST.get("item_id")  # Changed from item_name to item_id
        quantity = request.POST.get("remove_quantity")
        
        try:
            quantity = int(quantity)
        except (TypeError, ValueError):
            return JsonResponse({"status": "error", "message": "Invalid quantity"})

        try: 
            order = Order.objects.get(id=order_id)
            try:
                order_item = OrderItem.objects.get(menu_item__id=item_id, order=order)
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
def submit_order(request: HttpResponse) -> JsonResponse:
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
        # address = request.POST.get("address", "")  # Optional, for delivery orders
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
                continue # Or handle error: return JsonResponse({"status": "error", "message": f"Menu item with id {item_id} not found"}, status=400)
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
def update_order(request: HttpResponse) -> JsonResponse:
    """
    Update the order details (e.g. items, quantities, note) by a diner before it's processed.
    Assumes the order status allows modification (e.g., 'PENDING').
    """
    if "diner_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)
        
    if request.method == "POST":
        order_id = request.POST.get("order_id")
        updated_items_ids = request.POST.getlist("item_ids")  # Expecting list of menu_item_ids
        updated_quantities = request.POST.getlist("quantities") # Matching list of quantities
        updated_note = request.POST.get("note", None) # Optional

        if not order_id:
            return JsonResponse({"status": "error", "message": "Order ID is required"}, status=400)
        if len(updated_items_ids) != len(updated_quantities):
            return JsonResponse({"status": "error", "message": "Items and quantities mismatch"}, status=400)

        try:
            order = Order.objects.get(id=order_id, diner_id=request.session["diner_id"])
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found or not yours"}, status=404)

        # Basic check if order can be updated (e.g., only if PENDING)
        if order.status != 'PENDING':
            return JsonResponse({"status": "error", "message": f"Order cannot be updated in '{order.status}' status"}, status=400)
        
        # Clear existing items for simplicity, or implement more complex diff logic
        order.order_items.all().delete()
        
        new_total_price = 0
        for item_id, qty_str in zip(updated_items_ids, updated_quantities):
            try:
                quantity = int(qty_str)
                if quantity <= 0:
                    continue # Skip items with zero or negative quantity
                menu_item = MenuItem.objects.get(id=item_id)
                OrderItem.objects.create(
                    order=order,
                    menu_item=menu_item,
                    quantity=quantity
                )
                new_total_price += menu_item.price * quantity
            except MenuItem.DoesNotExist:
                # Rollback or decide handling: for now, skip unknown items
                # For a transactional approach, consider `django.db.transaction.atomic`
                return JsonResponse({"status": "error", "message": f"Menu item with id {item_id} not found, update failed."}, status=400)
            except ValueError:
                return JsonResponse({"status": "error", "message": f"Invalid quantity for item id {item_id}"}, status=400)
        
        order.total_price = new_total_price
        if updated_note is not None:
            order.note = updated_note
        order.last_modified = timezone.now()
        order.save()
        
        return JsonResponse({
            "status": "success", 
            "message": "Order updated successfully",
            "order_id": order.id,
            "total_price": order.total_price
        })
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
def get_order_status(request: HttpResponse) -> JsonResponse:
    """
    Get the status and details of a specific order.
    Diners can only see their own orders. Staff might see any.
    """
    if "diner_id" in request.session:
        try:
            order_id = request.GET.get("order_id")
            if not order_id:
                return JsonResponse({"status": "error", "message": "Order ID is required"}, status=400)
            order = Order.objects.get(id=order_id, diner_id=request.session["diner_id"])
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found or not authorized"}, status=404)
    elif "staff_id" in request.session: # Assuming staff can view any order
        try:
            order_id = request.GET.get("order_id")
            if not order_id:
                return JsonResponse({"status": "error", "message": "Order ID is required"}, status=400)
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"}, status=404)
    else:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)

    if request.method == "GET":
        order_items = list(order.order_items.values('menu_item__name', 'quantity', 'menu_item__price'))
        return JsonResponse({
            "status": "success",
            "order_id": order.id,
            "order_status": order.status,
            "service_type": order.service_type,
            "note": order.note,
            "total_price": order.total_price,
            "time_created": order.time_created.strftime('%Y-%m-%d %H:%M:%S'),
            "last_modified": order.last_modified.strftime('%Y-%m-%d %H:%M:%S'),
            "items": order_items
        })
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
def update_order_status_by_staff(request: HttpResponse) -> JsonResponse:
    """
    Update the status of an order (e.g., from PENDING to COMPLETED).
    This action should be restricted to staff members.
    """
    if "staff_id" not in request.session: # Check if staff is logged in
        return JsonResponse({"status": "error", "message": "Not authorized. Staff access required."}, status=403)

    if request.method == "POST":
        order_id = request.POST.get("order_id")
        new_status = request.POST.get("status")

        if not order_id or not new_status:
            return JsonResponse({"status": "error", "message": "Order ID and new status are required"}, status=400)

        # Validate new_status against Order.STATUS_CHOICES
        valid_statuses = [choice[0] for choice in Order.STATUS_CHOICES]
        if new_status not in valid_statuses:
            return JsonResponse({"status": "error", "message": f"Invalid status. Must be one of {valid_statuses}"}, status=400)

        try:
            order = Order.objects.get(id=order_id)
            order.status = new_status
            order.last_modified = timezone.now()
            order.save()
            # Potentially trigger notifications or other actions here
            return JsonResponse({"status": "success", "message": f"Order {order_id} status updated to {new_status}"})
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
def get_diner_orders(request: HttpResponse) -> JsonResponse:
    """
    Get all orders for a specific diner.
    Ensures the logged-in diner can only access their own orders, or staff can access.
    """
    # Security check: Logged-in diner must match diner_id or be staff
    diner_id = request.GET.get("diner_id")
    if not diner_id:
        return JsonResponse({"status": "error", "message": "Diner ID is required"}, status=400)
    if "diner_id" in request.session and request.session["diner_id"] == diner_id:
        pass # Diner is accessing their own orders
    elif "staff_id" in request.session:
        pass # Staff can access any diner's orders
    else:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)

    if request.method == "GET":
        try:
            diner = Diner.objects.get(id=diner_id)
            orders = Order.objects.filter(diner=diner).order_by('-time_created')
            orders_data = []
            for order in orders:
                items = list(order.order_items.values('menu_item__name', 'quantity', 'menu_item__price'))
                orders_data.append({
                    "order_id": order.id,
                    "status": order.status,
                    "total_price": order.total_price,
                    "time_created": order.time_created.strftime('%Y-%m-%d %H:%M:%S'),
                    "items_count": sum(item['quantity'] for item in items) # Example: total items
                })
            return JsonResponse({"status": "success", "diner_id": diner_id, "orders": orders_data})
        except Diner.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Diner not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
def get_all_orders(request: HttpResponse) -> JsonResponse:
    """
    Get all orders. Restricted to staff members.
    """
    if "staff_id" not in request.session: # Check if staff is logged in
        return JsonResponse({"status": "error", "message": "Not authorized. Staff access required."}, status=403)

    if request.method == "GET":
        orders = Order.objects.all().order_by('-time_created')
        orders_data = []
        for order in orders:
            items = list(order.order_items.values('menu_item__name', 'quantity'))
            orders_data.append({
                "order_id": order.id,
                "diner_id": order.diner.id,
                "status": order.status,
                "service_type": order.service_type,
                "total_price": order.total_price,
                "time_created": order.time_created.strftime('%Y-%m-%d %H:%M:%S'),
                "items_count": sum(item['quantity'] for item in items)
            })
        return JsonResponse({"status": "success", "orders": orders_data})
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
def get_kitchen_orders(request: HttpResponse) -> JsonResponse:
    """
    Get orders relevant to the kitchen (e.g., PENDING, PREPARING).
    Restricted to staff members.
    """
    if "staff_id" not in request.session: # Check if staff is logged in
        return JsonResponse({"status": "error", "message": "Not authorized. Staff access required."}, status=403)

    if request.method == "GET":
        # Define kitchen-relevant statuses. This might expand if you add more statuses like 'PREPARING'.
        kitchen_statuses = ['PENDING'] 
        orders = Order.objects.filter(status__in=kitchen_statuses).order_by('time_created') # Oldest pending first
        
        orders_data = []
        for order in orders:
            items_details = list(order.order_items.values('menu_item__name', 'quantity', 'menu_item__description'))
            orders_data.append({
                "order_id": order.id,
                "service_type": order.service_type,
                "note": order.note,
                "time_created": order.time_created.strftime('%Y-%m-%d %H:%M:%S'),
                "items": items_details
            })
        return JsonResponse({"status": "success", "kitchen_orders": orders_data})
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

# Example of a view for processing payments (not fully detailed in urls.py yet)
@csrf_exempt
def process_payment(request: HttpResponse) -> JsonResponse:
    if "diner_id" not in request.session:
         return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)

    if request.method == "POST":
        order_id = request.POST.get("order_id")
        payment_method = request.POST.get("payment_method") # e.g., 'CASH', 'ONLINE_BANKING'

        if not order_id or not payment_method:
            return JsonResponse({"status": "error", "message": "Order ID and payment method are required"}, status=400)
        
        valid_methods = [choice[0] for choice in Payment.METHOD_CHOICES]
        if payment_method not in valid_methods:
            return JsonResponse({"status": "error", "message": f"Invalid payment method. Must be one of {valid_methods}"}, status=400)

        try:
            order = Order.objects.get(id=order_id, diner_id=request.session["diner_id"])
            if order.status == 'COMPLETED':
                 return JsonResponse({"status": "error", "message": "Order already completed and paid"}, status=400)
            if order.status == 'CANCELED':
                 return JsonResponse({"status": "error", "message": "Cannot pay for a canceled order"}, status=400)

            # Check if payment already exists
            if hasattr(order, 'payment') and order.payment.status == 'paid':
                return JsonResponse({"status": "success", "message": "Order already paid"})

            # Create or update payment record
            payment, created = Payment.objects.update_or_create(
                order=order,
                defaults={'method': payment_method, 'status': 'paid'} # Mark as paid
            )
            
            # Update order status to COMPLETED upon successful payment
            order.status = 'COMPLETED'
            order.save()
            
            return JsonResponse({"status": "success", "message": "Payment successful", "payment_id": payment.id, "order_status": order.status})
        except Order.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)