from rest_framework import serializers
from .models import Menu, MenuItem

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        # fields = ('id', 'name', 'description')
        fields = '__all__'

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        # fields = ('id', 'name', 'description', 'price', 'menu_id')
        fields = '__all__'
