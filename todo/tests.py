from django.test import TestCase
from todo.models import Todo
from user.models import User 


class TodoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username="testuser",
            email="test@user.com",
            password="testuserpassword"
        )

        cls.todo_1 = Todo.objects.create(
            title="Todo1",
            user=cls.user,
            description="Some Content",
        )

        cls.todo_2 = Todo.objects.create(
            title="Todo2",
            user=cls.user,
            complete=True
        )

    def test_todo_model(self):
        self.assertEqual(self.todo_1.title, "Todo1")
        self.assertEqual(self.todo_1.user, self.user)
        self.assertEqual(self.todo_1.description, "Some Content")
        self.assertFalse(self.todo_1.complete)
        self.assertEqual(str(self.todo_1), "Todo1")

        self.assertEqual(self.todo_2.title, "Todo2")
        self.assertEqual(self.todo_2.user, self.user)
        self.assertEqual(self.todo_2.description, "")
        self.assertTrue(self.todo_2.complete)
        self.assertEqual(str(self.todo_2), "Todo2")


        todos = self.user.todos.all()
        self.assertIn(self.todo_1, todos)
        self.assertIn(self.todo_2, todos)