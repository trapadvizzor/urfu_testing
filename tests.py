import unittest
from flask import Flask, request
from unittest.mock import patch

# Функция, которую мы тестируем
def generate_words(n, length):
    # Это заглушка, настоящая реализация не предоставлена
    return []

class TestSuggestFunction(unittest.TestCase):
    def setUp(self):
        # Инициализация Flask-приложения
        self.app = Flask(__name__)

        @self.app.route('/suggest', methods=['GET'])
        def suggest():
            prefix = request.args.get('w', '')
            WORDS = generate_words(10000, 9)
            suggestions = [word for word in WORDS if word.startswith(prefix)]
            return '\n'.join(suggestions) + '\n'

        # Тестовый клиент
        self.client = self.app.test_client()

    def test_suggest_with_valid_prefix(self):
        # Mocking слов
        with patch('__main__.generate_words', return_value=['apple', 'apricot', 'banana']):
            response = self.client.get('/suggest?w=ap')
            self.assertEqual(response.data.decode(), 'apple\napricot\n')

    def test_suggest_with_invalid_prefix(self):
        with patch('__main__.generate_words', return_value=['apple', 'apricot', 'banana']):
            response = self.client.get('/suggest?w=xyz')
            self.assertEqual(response.data.decode(), '\n')

    def test_suggest_without_prefix(self):
        with patch('__main__.generate_words', return_value=['apple', 'apricot', 'banana']):
            response = self.client.get('/suggest')
            self.assertEqual(response.data.decode(), 'apple\napricot\nbanana\n')

    def test_suggest_with_empty_word_list(self):
        with patch('__main__.generate_words', return_value=[]):
            response = self.client.get('/suggest?w=ap')
            self.assertEqual(response.data.decode(), '\n')

    def test_suggest_with_prefix_matching_whole_word(self):
        with patch('__main__.generate_words', return_value=['apple', 'apricot']):
            response = self.client.get('/suggest?w=apple')
            self.assertEqual(response.data.decode(), 'apple\n')

    def test_suggest_with_uppercase_prefix(self):
        with patch('__main__.generate_words', return_value=['Apple', 'apricot']):
            response = self.client.get('/suggest?w=Ap')
            self.assertEqual(response.data.decode(), 'Apple\n')

    def test_suggest_performance(self):
        # This is just a basic performance test setup.
        # In reality, you'd measure time taken for completion.
        words = ['word' + str(i) for i in range(10000)]
        with patch('__main__.generate_words', return_value=words):
            response = self.client.get('/suggest?w=word')
            self.assertTrue(len(response.data.decode()) > 0)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
