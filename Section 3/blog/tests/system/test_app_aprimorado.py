from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog

MENU_PROMPT = "Options: \n'c' to create a blog\n'l' to list blogs\n'r' to read one\n'p' to create a post\n'q' to quit\n"

class AppTest(TestCase):
        
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}

# um dos modos de fazer, verificando a operação gerada
    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test', 'Test Author', 'q')
            
            app.menu()

            self.assertIsNotNone(app.blogs.get('Test'))
    
    
    # modo mais efetivo de se fazer o teste, verificando a função chamada
    def test_menu_calls_create_blog_2(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                mocked_input.side_effect = ('c', 'q')
                
                app.menu()

                mocked_ask_create_blog.assert_called()


    def test_menu_calls_read_blog(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_read_blog') as mocked_ask_read_blog:
                mocked_input.side_effect = ('r', 'q')
                
                app.menu()

                mocked_ask_read_blog.assert_called()


    def test_menu_calls_print_blogs(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.print_blogs') as mocked_print_blogs:
                mocked_input.side_effect = ('l', 'q')
                
                app.menu()

                mocked_print_blogs.assert_called()


    def test_menu_calls_create_post(self):
        with patch('builtins.input') as mocked_input:
            with patch('app.ask_create_post') as mocked_ask_create_post:
                mocked_input.side_effect = ('p', 'q')
                
                app.menu()

                mocked_ask_create_post.assert_called()


    def test_input_menu(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()

            mocked_input.assert_called_with(MENU_PROMPT)


    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value = 'q'):
                app.menu()
                mocked_print_blogs.assert_called()


    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()

            mocked_print.assert_called_with('- Test')


    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))


    def test_ask_read_blog(self):   
        with patch('builtins.input', return_value='Test'):
            with patch('builtins.print') as mocked_print:
                app.ask_read_blog()

                mocked_print.assert_called_with("Reading the Test's posts:\n")


    def test_app_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Title', 'Test Content')

            app.ask_create_post()

            blog_post = str(app.blogs['Test'].posts[0])

            expected = '<title: Test Title, content: Test Content>'

            self.assertEqual(blog_post, expected)
            