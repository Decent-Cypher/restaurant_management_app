from django.shortcuts import render
from .models import Menu, MenuItem
from .serializers import MenuSerializer, MenuItemSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets

# Create your views here.
class MenuViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing menu instances.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuItemViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing menu item instances.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
        