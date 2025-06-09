"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

# Import views from all apps
from accounts import views as account_views
from menu import views as menu_views
from orders import views as order_views
from reviews import views as review_views
from analytics import views as analytics_views 

# Routers for ViewSets
menu_router = DefaultRouter()
menu_router.register(r'menus', menu_views.MenuViewSet, basename='menu')
menu_router.register(r'menu-items', menu_views.MenuItemViewSet, basename='menuitem')

review_router = DefaultRouter()
review_router.register(r'feedbacks', review_views.FeedbackViewSet, basename='feedback')


urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts URLs
    path('api/accounts/staff/login/', account_views.staff_login, name='staff_login'),
    path('api/accounts/diner/login/', account_views.diner_login, name='diner_login'),
    path('api/accounts/logout/', account_views.logout_view, name='logout'),
    path('api/accounts/protected/', account_views.protected_view, name='protected'),
    path('api/accounts/diner/info/', account_views.get_diner_info, name='get_diner_info'),

    # Menu URLs (using router)
    path('api/menu/', include(menu_router.urls)),

    # Orders URLs
    path('api/orders/get_order/', order_views.get_order_by_id, name='get_order_by_id'),
    path('api/orders/items/add/', order_views.add_order_item, name='add_order_item'),
    path('api/orders/items/remove/', order_views.remove_order_item, name='remove_order_item'),
    path('api/orders/note/add/', order_views.add_note, name='add_note'),
    path('api/orders/service/choose/', order_views.choose_service, name='choose_service'),
    path('api/orders/submit/', order_views.submit_order, name='submit_order'),
    path('api/orders/update/', order_views.update_order, name='update_order'),
    path('api/orders/status/update/', order_views.update_order_status_by_staff, name='update_order_status_by_staff'),
    path('api/orders/status/', order_views.get_order_status, name='get_order_status'),
    path('api/orders/diner/', order_views.get_diner_orders, name='get_diner_orders'),
    path('api/orders/all/', order_views.get_all_orders, name='get_all_orders'),
    path('api/orders/kitchen/', order_views.get_kitchen_orders, name='get_kitchen_orders'),
    path('api/orders/pay/', order_views.process_payment, name='pay_for_order'),
    # Reviews URLs (using router)
    path('api/reviews/', include(review_router.urls)),

    # Analytics URLs
    path('api/analytics/rating/', analytics_views.get_rating_analytics, name='get_rating_analytics'),
    path('api/analytics/revenue/', analytics_views.get_revenue_analytics, name='get_revenue_analytics'),
    path('api/analytics/order-count/', analytics_views.get_menu_items_order_count, name='get_order_count'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)