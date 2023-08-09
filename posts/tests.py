from django.test import TestCase
from .models import Post
from django.urls import reverse

class PostModelTest(TestCase):

    def setUp(self) -> None:
        Post.objects.create(text='just a text')
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post}'
        self.assertEqual(expected_object_name, 'just a text')

class HomePageViewTest(TestCase):

    def setUp(self) -> None:
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/post/')
        self.assertEquals(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get('/post/')
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('posts:home_p'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'home_p.html')