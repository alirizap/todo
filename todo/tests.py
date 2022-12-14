from django.test import TestCase
from todo.models import Todo
from user.models import User
from category.models import Category 


class TodoTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username="testuser",
            email="test@user.com",
            password="testuserpassword"
        )

        cls.shopping_category = Category.objects.create(
            name="Shopping"
        )

        cls.travel_category = Category.objects.create(
            name="Travel"
        )

        cls.homework_category = Category.objects.create(
            name="Homework"
        )

        cls.todo_1 = Todo.objects.create(
            title="Todo1",
            user=cls.user,
            description="Some Content",
        )
        cls.todo_1.category.add(cls.shopping_category)
        cls.todo_1.category.add(cls.travel_category)

        cls.todo_2 = Todo.objects.create(
            title="Todo2",
            user=cls.user,
            complete=True
        )
        cls.todo_2.category.add(cls.homework_category)

    def test_todo_model(self):
        self.assertEqual(self.todo_1.title, "Todo1")
        self.assertEqual(self.todo_1.user, self.user)
        self.assertEqual(self.todo_1.description, "Some Content")
        self.assertFalse(self.todo_1.complete)
        self.assertEqual(str(self.todo_1), "Todo1")
        self.assertEqual(self.todo_1.category.count(), 2)
        self.assertEqual(self.todo_1.category.get(name="Shopping"), self.shopping_category)
        self.assertEqual(self.todo_1.category.get(name="Travel"), self.travel_category)

        self.assertEqual(self.todo_2.title, "Todo2")
        self.assertEqual(self.todo_2.user, self.user)
        self.assertEqual(self.todo_2.description, "")
        self.assertTrue(self.todo_2.complete)
        self.assertEqual(str(self.todo_2), "Todo2")
        self.assertEqual(self.todo_2.category.count(), 1)
        self.assertEqual(self.todo_2.category.get(name="Homework"), self.homework_category)


        todos = self.user.todos.all()
        self.assertIn(self.todo_1, todos)
        self.assertIn(self.todo_2, todos)