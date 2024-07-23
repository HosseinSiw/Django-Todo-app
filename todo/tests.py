from django.test import TestCase
from .models import Todo


class TodoModelTest(TestCase):
    def test_str_method(self):
        todo = Todo.objects.create(title='Test Title', user_id=1)
        self.assertEqual(str(todo), 'Test Title')

