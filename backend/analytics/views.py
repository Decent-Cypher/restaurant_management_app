from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.db.models import Sum
from reviews.models import Feedback  # Assumes the Feedback model is in the reviews app
from orders.models import Order, OrderItem


@csrf_exempt
def get_mean_rating(request: HttpRequest) -> JsonResponse:
    """
    Returns the mean rating for feedbacks within a given time range.
    Expects 'start' and 'end' query parameters in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    if request.method != "GET":
        return JsonResponse({"status": "error", "message": "Invalid HTTP method"}, status=405)
    
    if "staff_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Unauthorized access"}, status=403)

    start = request.GET.get("start")
    end = request.GET.get("end")
    
    if not start or not end:
        return JsonResponse({"status": "error", "message": "start and end parameters are required"}, status=400)
    
    try:
        start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return JsonResponse({
            "status": "error",
            "message": "Invalid datetime format, use YYYY-MM-DD HH:MM:SS"
        }, status=400)
    
    feedbacks = Feedback.objects.filter(time_created__range=(start_dt, end_dt)).values_list('rating', flat=True)
    ratings = list(feedbacks)
    
    if not ratings:
        mean_rating = 0
    else:
        mean_rating = sum(ratings) / len(ratings)
    
    return JsonResponse({"status": "success", "mean_rating": mean_rating})


@csrf_exempt
def get_total_revenue(request: HttpRequest) -> JsonResponse:
    """
    Returns the total revenue (sum of order total prices) within a given time range.
    Expects 'start' and 'end' query parameters in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    if request.method != "GET":
        return JsonResponse({"status": "error", "message": "Invalid HTTP method"}, status=405)
    
    if "staff_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Unauthorized access"}, status=403)

    start = request.GET.get("start")
    end = request.GET.get("end")
    
    if not start or not end:
        return JsonResponse({"status": "error", "message": "start and end parameters are required"}, status=400)
    
    try:
        start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return JsonResponse({
            "status": "error",
            "message": "Invalid datetime format, use YYYY-MM-DD HH:MM:SS"
        }, status=400)
    
    orders = Order.objects.filter(time_created__range=(start_dt, end_dt))
    revenue = orders.aggregate(total_revenue=Sum('total_price'))["total_revenue"] or 0
    
    return JsonResponse({"status": "success", "total_revenue": revenue})


@csrf_exempt
def get_menu_items_order_count(request: HttpRequest) -> JsonResponse:
    """
    Returns the count of ordered menu items within a given time range.
    Expects 'start' and 'end' query parameters in the format 'YYYY-MM-DD HH:MM:SS'.
    Returns a list of menu item names and their total order quantities.
    """
    if request.method != "GET":
        return JsonResponse({"status": "error", "message": "Invalid HTTP method"}, status=405)
    
    if "staff_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Unauthorized access"}, status=403)

    start = request.GET.get("start")
    end = request.GET.get("end")
    
    if not start or not end:
        return JsonResponse({"status": "error", "message": "start and end parameters are required"}, status=400)
    
    try:
        start_dt = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        end_dt = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return JsonResponse({
            "status": "error",
            "message": "Invalid datetime format, use YYYY-MM-DD HH:MM:SS"
        }, status=400)
    
    order_items = OrderItem.objects.filter(order__last_modified__range=(start_dt, end_dt))
    counts = order_items.values("menu_item__id").annotate(order_count=Sum("quantity"))
    result = list(counts)
    
    return JsonResponse({"status": "success", "menu_items_order_count": result})

