from lyric_analyzer import LyricAnalyzer
from stop_words import StopWord
import unittest
from unittest.mock import MagicMock
from helper_variables import TOP_THREE_WORDS, TOP_THREE_WORDS_TITLE_AND_URL, TOP_ARTICLES_RESPONSE, ARTICLE_INFO
import pdb
import copy

class TestLyricAnalyzer(unittest.TestCase):
    def test_example(self):
        thing = LyricAnalyzer('lyric', 3)
        thing.method = MagicMock(return_value=3)
        thing.method(3, 4, 5, key='value')

        thing.method.assert_called_with(3, 4, 5, key='value')
        self.assertEqual(thing.method(3,4,5), 3)

    def test_top_words(self):
        lyric_analyzer = LyricAnalyzer('lyrics', 3)
        words = ['apple', 'apple', 'apple', 'apple', 'orange', 'orange', 'orange', 'orange', 'bag', 'bag', 'bag', 'nail', 'bed']
        lyric_analyzer.clean = MagicMock(return_value=words)
        output = TOP_THREE_WORDS
        self.assertEqual(lyric_analyzer.top_words(), output)

    def test_top_articles(self):
        lyric_analyzer = LyricAnalyzer('lyrics', 3)
        #Mock top_words()
        top = copy.deepcopy(TOP_THREE_WORDS)
        lyric_analyzer.top_words = MagicMock(return_value=top)
        self.assertEqual(lyric_analyzer.top_words(), top)
        #Mock get_info()
        info = ARTICLE_INFO
        lyric_analyzer.get_info = MagicMock(return_value=info)
        #Isolate top_articles() functionality
        response = TOP_ARTICLES_RESPONSE
        self.assertEqual(lyric_analyzer.top_articles(), response)


if __name__ == '__main__':
    unittest.main()

'''May help testing get_info()

        titles_and_urls = TOP_THREE_WORDS_TITLE_AND_URL
        for i in range(0, len(top)):
            pdb.set_trace()
            lyric_analyzer.get_info = MagicMock(return_value=titles_and_urls[i])
            self.assertEqual(lyric_analyzer.get_info(), titles_and_urls[i])
'''
