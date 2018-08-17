from news_client import NewsClient
import unittest
from unittest.mock import MagicMock
from helper_variables import TOP_ARTICLES_RESPONSE, TOP_ARTICLES, TOP_ARTICLE, TITLE_AND_URL
import pdb

class TestNewsClient(unittest.TestCase):
    def test_example(self):
        thing = NewsClient('keyword')
        thing.method = MagicMock(return_value=3)
        thing.method(3, 4, 5, key='value')

        thing.method.assert_called_with(3, 4, 5, key='value')
        self.assertEqual(thing.method(3,4,5), 3)

    '''TODO
    *stub api call and return list of articles
    *change response for not find an article
        *add corresponding tests for failure
    '''
    def get_top_articles(self):
        pass

    def test_top_random_article(self):
        api = NewsClient('keyword')
        response = TOP_ARTICLES_RESPONSE
        top_articles = TOP_ARTICLES
        api.get_top_articles = MagicMock(return_value=response)
        self.assertTrue(api.random_top_article() in TOP_ARTICLES)

    def test_parse_title_and_url(self):
        api = NewsClient('keyword')
        top_article = TOP_ARTICLE
        api.random_top_article = MagicMock(return_value=top_article)
        output = TITLE_AND_URL
        self.assertEqual(api.parse_title_and_url(), output)

if __name__ == '__main__':
    unittest.main()
