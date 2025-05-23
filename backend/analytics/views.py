from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback  # Ensure this is the correct import path

@csrf_exempt  # Remove or modify for production
def list_feedback(request: HttpRequest) -> JsonResponse:
    """
    List all feedback data. Only available for logged-in staff.
    """
    if request.method != "GET":
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
    
    if "staff_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)
    
    feedback_qs = Feedback.objects.all()
    feedback_list = []
    for fb in feedback_qs:
        feedback_list.append({
            "id": fb.id,
            "order_id": fb.order.id if fb.order else None,
            "rating": fb.rating,
            "comment": fb.comment,
            "created": fb.created.strftime("%Y-%m-%d %H:%M:%S")
        })
    
    return JsonResponse({"status": "success", "feedback": feedback_list})


@csrf_exempt  # Remove or modify for production
def get_feedback_detail(request: HttpRequest, feedback_id: int) -> JsonResponse:
    """
    Get detailed feedback data for a specific feedback entry.
    """
    if request.method != "GET":
        return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)
    
    if "staff_id" not in request.session:
        return JsonResponse({"status": "error", "message": "Not authorized"}, status=403)
    
    try:
        fb = Feedback.objects.get(id=feedback_id)
    except Feedback.DoesNotExist:
        return JsonResponse({"status": "error", "message": "Feedback not found"}, status=404)
    
    data = {
        "id": fb.id,
        "order_id": fb.order.id if fb.order else None,
        "rating": fb.rating,
        "comment": fb.comment,
        "created": fb.created.strftime("%Y-%m-%d %H:%M:%S")
    }
    return JsonResponse({"status": "success", "feedback": data})