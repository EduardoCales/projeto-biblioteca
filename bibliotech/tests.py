from django.test import TestCase
from django.urls import reverse


class BibliotechURLsTest(TestCase):
    def test_bibliotech_home_url_is_correct(self):
        url = reverse('livros:home')
        self.assertEqual(url, '/')

    def test_bibliotech_category_url_is_correct(self):
        url = reverse('livros:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/livros/category/1/')

    def test_bibliotech_livro_url_is_correct(self):
        url = reverse('livros:livro', kwargs={'id': 1})
        self.assertEqual(url, '/livros/1/')