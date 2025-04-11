from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django for APIs",
            subtitle="Build web APIs with Python and Django",
            author="William S. Vincent",
            isbn="9781735467221",
        )
        cls.book_data = {
            "title": "New Book",
            "subtitle": "A new subtitle",
            "author": "New Author",
            "isbn": "1234567890123",
        }

    def test_api_listview(self):
        response = self.client.get(reverse("book_list_create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)

    def test_api_create_book(self):
        response = self.client.post(reverse("book_list_create"), self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_api_get_book_detail(self):
        response = self.client.get(reverse("book_detail", kwargs={"pk": self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.book.title)

    def test_api_update_book(self):
        updated_data = {
            "title": "Updated Title",
            "subtitle": "Updated Subtitle",
            "author": "Updated Author",
            "isbn": "9781735467221",
        }
        response = self.client.put(reverse("book_detail", kwargs={"pk": self.book.id}), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")

    def test_api_delete_book(self):
        response = self.client.delete(reverse("book_detail", kwargs={"pk": self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)