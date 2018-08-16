from lyric_analyzer import LyricAnalyzer
from stop_words import StopWord
import unittest
from unittest.mock import MagicMock
from helper_variables import TOP_THREE_ARTICLES
import pdb

class TestLyricAnalyzer(unittest.TestCase):
    def test_example(self):
        thing = LyricAnalyzer('lyric', 3)
        thing.method = MagicMock(return_value=3)
        thing.method(3, 4, 5, key='value')

        thing.method.assert_called_with(3, 4, 5, key='value')
        self.assertEqual(thing.method(3,4,5), 3)

    def test_top_words(self):
        lyric_analyzer = LyricAnalyzer('lyrics', 3)
        words=['apple', 'apple', 'apple', 'apple', 'orange', 'orange', 'orange', 'orange', 'bag', 'bag', 'bag', 'nail', 'bed']
        lyric_analyzer.clean = MagicMock(return_value=words)
        output = TOP_THREE_ARTICLES
        self.assertEqual(lyric_analyzer.top_words(), output)
if __name__ == '__main__':
    unittest.main()

