import io
import pytest
from PIL import Image
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status
from menu.models import Menu

@pytest.mark.django_db
class TestMenuAPI:
    def generate_image_file(self, name='test.jpg', size=(100, 100), color=(255, 0, 0)):
        file = io.BytesIO()
        image = Image.new('RGB', size, color)
        image.save(file, 'JPEG')
        file.name = name
        file.seek(0)
        return file

    def test_create_menu(self, client):
        image_file = self.generate_image_file()
        uploaded_file = SimpleUploadedFile(image_file.name, image_file.read(), content_type='image/jpeg')
        data = {
            'name': 'Lunch Menu',
            'description': 'Delicious lunch options',
            'image': uploaded_file
        }
        url = reverse('menu-list')
        response = client.post(url, data, format='multipart')
        assert response.status_code == status.HTTP_201_CREATED
        assert Menu.objects.count() == 1
        menu = Menu.objects.first()
        assert menu is not None
        assert menu.name == 'Lunch Menu'

    def test_list_menus(self, client):
        Menu.objects.create(
            name='Dinner Menu',
            description='Evening meals',
            image=SimpleUploadedFile('dinner.jpg', b'file_content', content_type='image/jpeg')
        )
        url = reverse('menu-list')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

    def test_retrieve_menu(self, client):
        menu = Menu.objects.create(
            name='Breakfast Menu',
            description='Morning meals',
            image=SimpleUploadedFile('breakfast.jpg', b'file_content', content_type='image/jpeg')
        )
        url = reverse('menu-detail', args=[menu.id])
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'Breakfast Menu'
