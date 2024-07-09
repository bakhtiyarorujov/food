from django.test import TestCase, Client
from django.urls import reverse_lazy
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from stories.models import Category, Tag
import os
from django.conf import settings

User = get_user_model()

class RecipeAPITest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        user = User.objects.create_user(username='john', email='john@mail.com', password='pass12345')
        tag = Tag.objects.create(name='Tag 1')
        category = Category.objects.create(name='Category 1')
        client = APIClient()
        refresh = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
        cls.url = reverse_lazy('api_recipe_list')
        cls.response = client.get(cls.url)
        file_path = os.path.join(settings.MEDIA_ROOT, 'recipe_cover/image_1.jpg') 
        cls.data = {
            'title': 'Recipe #500',
            'content': 'test content',
            'tags': tag.id,
            'category': category.id,
            'cover':  (open(file_path, 'rb'),)
        }
        cls.post_valid = client.post(cls.url, data=cls.data)

    def test_url(self):
        self.assertEqual(self.url, '/api/recipes')

    def test_response_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_post_status_code(self):
        self.assertEqual(self.post_valid.status_code, 201)


    @classmethod
    def tearDownClass(cls) -> None:
        pass