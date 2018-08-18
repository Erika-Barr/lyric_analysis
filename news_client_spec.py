from news_client import NewsClient
import unittest
from unittest.mock import MagicMock
from helper_variables import TOP_ARTICLES_RESPONSE, TOP_ARTICLES, TOP_ARTICLE, TITLE_AND_URL, TOP_HEADLINE_RESPONSE
import os
import pdb

class TestNewsClient(unittest.TestCase):
    '''TODO
    *stub api call and return list of articles
    *change response for not find an article
        *add corresponding tests for failure
    '''
    # Check that external api is being called.
    def test_get_top_articles(self):
        api = NewsClient('keyword')
        response = TOP_HEADLINE_RESPONSE
        api.news_api.get_top_headlines = MagicMock(return_value=response)
        self.assertEqual(api.get_top_articles(), TOP_HEADLINE_RESPONSE)

    def test_top_random_article(self):
        api = NewsClient('keyword')
        response = TOP_HEADLINE_RESPONSE
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
