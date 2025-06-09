from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Staff, Diner

@csrf_exempt  # For testing; handle CSRF properly in production
def staff_login(request: HttpRequest) -> JsonResponse:
    """
    Example staff login view that sets a session cookie on success.
    """
    # print(request.session.keys())
    # print(request.session.items())
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            staff = Staff.objects.get(name=username)
        except Staff.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=400)

        if staff.check_password(password):
            # Store staff ID in session
            request.session['staff_id'] = staff.id
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=400)

    return JsonResponse({'error': 'Only POST allowed'}, status=405)

@csrf_exempt
def diner_login(request: HttpRequest) -> JsonResponse:
    
    # print(request.session.keys())
    # print(request.session.items())
    """
    Example diner login view that sets a session cookie on success.
    """
    print(request.session.items())
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            diner = Diner.objects.get(name=username)
        except Diner.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=400)
        if diner.check_password(password):
            # Store diner ID in session
            request.session['diner_id'] = diner.id
            print(request.session.items())
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid credentials'}, status=400)
    return JsonResponse({'error': 'Only POST allowed'}, status=405)

@csrf_exempt
def logout_view(request: HttpRequest) -> JsonResponse:
    """
    Logs out either a staff or diner by clearing the session.
    """
    if request.method == 'POST':
        try:
            request.session.flush()  # Clears all session data
            return JsonResponse({'success': True}, status = 200)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    return JsonResponse({'error': 'Only POST allowed'}, status=405)

@csrf_exempt
def protected_view(request: HttpRequest) -> JsonResponse:
    """
    Example view that requires a staff or diner to be logged in.
    """
    print(request.session)
    if 'staff_id' in request.session:
        staff = Staff.objects.get(id=request.session['staff_id'])
        # Check if staff has manager role by querying the database
        return JsonResponse({'success': True, 'message': 'Hello Staff Bro', 'staff_id': request.session['staff_id'], 'role': staff.role})
    elif 'diner_id' in request.session:
        return JsonResponse({'success': True, 'message': 'Hello Diner Bro', 'diner_id': request.session['diner_id'], 'role': 'Diner'})
    return JsonResponse({'success': False, 'error': 'Not logged in'}, status=403)

@csrf_exempt
def get_diner_info(request: HttpRequest) -> JsonResponse:
    """
    Returns diner information
    """
    if request.method == "GET":
        if 'diner_id' in request.session:
            diner_id = request.GET.get('diner_id')
            try:
                diner = Diner.objects.get(id=diner_id)
            except Diner.DoesNotExist:
                return JsonResponse({"status": "error", "message": "Diner not found"}, status=404)
            return JsonResponse({
                "status": "success",
                "diner_info": {
                    "name": diner.name,
                    "email": diner.email,
                    "phone_number": diner.phone_num,
                }
            })
        else:
            return JsonResponse({"status": "error", "message": "Unauthorized access"}, status=403)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


@csrf_exempt
def add_accounts(request: HttpRequest) -> JsonResponse:
    """
    Add account for new staff -> Store to diner database
    """
    if request.method == "POST":
        if 'staff_id' in request.session:
            staff = Staff.objects.get(id=request.session['staff_id'])
            if staff.role == 'Manager':
                name = request.POST.get("name")
                role = request.POST.get("role")
                email = request.POST.get("email")
                if not name or not role or not email:
                    return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)
                if not role in ['Manager', 'Waiter', 'Chef']:
                    return JsonResponse({"status": "error", "message": "Invalid role"}, status=400)
                new_staff = Staff(
                    name=name,
                    role=role,
                    email=email,
                )
                new_staff.save()
                return JsonResponse({"status": "success", "message": "Staff account created successfully"}, status=201)
            else:
                return JsonResponse({"status": "error", "message": "Unauthorized access"}, status=403)
        else:
            return JsonResponse({"status": "error", "message": "Unauthorized access"}, status=403)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)


@csrf_exempt
def delete_accounts(request: HttpRequest) -> JsonResponse:
    """
    Delete staff accounts
    """
    if request.method == "POST":
        if 'staff_id' in request.session:
            staff = Staff.objects.get(id=request.session['staff_id'])
            if staff.role == 'Manager':
                staff_id = request.POST.get("staff_id")
                if not staff_id:
                    return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)
                try:
                    staff_to_delete = Staff.objects.get(id=staff_id)
                    staff_to_delete.delete()
                    return JsonResponse({"status": "success", "message": "Staff account deleted successfully"}, status=200)
                except Staff.DoesNotExist:
                    return JsonResponse({"status": "error", "message": "Staff not found"}, status=404)
            else:
                return JsonResponse({"status": "error", "message": "Unauthorized access"}, status=403)
        else:
            return JsonResponse({"status": "error", "message": "Unauthorized access"}, status=403)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
def update_roles(request: HttpRequest) -> JsonResponse:
    """
    Update staff roles
    """
    if request.method == "POST":
        if 'staff_id' in request.session:
            staff = Staff.objects.get(id=request.session['staff_id'])
            if staff.role == 'Manager':
                staff_id = request.POST.get("staff_id")
                new_role = request.POST.get("new_role")
                if not staff_id or not new_role:
                    return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)
                if new_role not in ['Manager', 'Waiter', 'Chef']:
                    return JsonResponse({"status": "error", "message": "Invalid role"}, status=400)
                try:
                    staff_to_update = Staff.objects.get(id=staff_id)
                    staff_to_update.role = new_role
                    staff_to_update.save()
                    return JsonResponse({"status": "success", "message": "Staff role updated successfully"}, status=200)
                except Staff.DoesNotExist:
                    return JsonResponse({"status": "error", "message": "Staff not found"}, status=404)
            else:
                return JsonResponse({"status": "error", "message": "Unauthorized access"}, status=403)
        else:
            return JsonResponse({"status": "error", "message": "Unauthorized access"}, status=403)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)