import io
import pytest
from PIL import Image
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from menu.models import Menu, MenuItem

@pytest.mark.django_db
class TestMenuItemAPI:
    def generate_image_file(self, name='item.jpg', size=(100, 100), color=(0, 255, 0)):
        file = io.BytesIO()
        image = Image.new('RGB', size, color)
        image.save(file, 'JPEG')
        file.name = name
        file.seek(0)
        return file

    def test_create_menu_item(self, client):
        menu = Menu.objects.create(
            name='Specials',
            description='Chef specials',
            image=SimpleUploadedFile('specials.jpg', b'file_content', content_type='image/jpeg')
        )
        image_file = self.generate_image_file()
        uploaded_file = SimpleUploadedFile(image_file.name, image_file.read(), content_type='image/jpeg')
        data = {
            'name': 'Grilled Salmon',
            'description': 'Freshly grilled salmon with herbs',
            'price': '15.99',
            'menu': menu.id,
            'image': uploaded_file
        }
        url = reverse('menuitem-list')
        response = client.post(url, data, format='multipart')
        assert response.status_code == status.HTTP_201_CREATED
        assert MenuItem.objects.count() == 1
        item = MenuItem.objects.first()
        assert item is not None
        assert item.name == 'Grilled Salmon'

    def test_list_menu_items(self, client):
        menu = Menu.objects.create(
            name='Desserts',
            description='Sweet treats',
            image=SimpleUploadedFile('desserts.jpg', b'file_content', content_type='image/jpeg')
        )
        MenuItem.objects.create(
            name='Chocolate Cake',
            description='Rich chocolate cake',
            price='5.50',
            menu=menu,
            image=SimpleUploadedFile('cake.jpg', b'file_content', content_type='image/jpeg')
        )
        url = reverse('menuitem-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_retrieve_menu_item(self, client):
        menu = Menu.objects.create(
            name='Beverages',
            description='Drinks',
            image=SimpleUploadedFile('beverages.jpg', b'file_content', content_type='image/jpeg')
        )
        item = MenuItem.objects.create(
            name='Lemonade',
            description='Fresh lemonade',
            price='2.99',
            menu=menu,
            image=SimpleUploadedFile('lemonade.jpg', b'file_content', content_type='image/jpeg')
        )
        url = reverse('menuitem-detail', args=[item.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'Lemonade'