from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

    def test_post(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post Title', 'Test Post Content')

        b2 = Blog('Generic', 'Generic Author')

        self.assertEqual(b.__repr__(), '<title: Test, author: Test Author, posts: 1>')
        self.assertEqual(b2.__repr__(), '<title: Generic, author: Generic Author, posts: 0>')


    def test_json_with_posts(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post Title', 'Test Post Content')

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [ { 'title': 'Test Post Title', 'content': 'Test Post Content' } ]
            }

        self.assertDictEqual(b.json(), expected)


    def test_json_without_posts(self):
        b = Blog('Test', 'Test Author')

        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': []
            }

        self.assertDictEqual(b.json(), expected)