from stop_words import StopWord
import unittest
from unittest.mock import MagicMock
import pdb

class TestStopWord(unittest.TestCase):
    def test_example(self):
        class Some(object): pass
        thing = Some()
        thing.method = MagicMock(return_value=3)
        thing.method(3, 4, 5, key='value')

        thing.method.assert_called_with(3, 4, 5, key='value')
        self.assertEqual(thing.method(3,4,5), 3)
    def test_clean(self):
        #text = "This is some text, representing songs lyrics, and, it needs to be filtered."
        text = "This is a sample sentence, showing off the stop words filtration."
        stop_word = StopWord(text)
        cleaned = ['This', 'is', 'a', 'sample', 'sentence', ',', 'showing', 'off', 'the', 'stop', 'words', 'filtration', '.']
        self.assertEqual(stop_word.clean(), cleaned)

    def test_remove(self):
        cleaned = ['This', 'is', 'a', 'sample', 'sentence', ',', 'showing', 'off', 'the', 'stop', 'words', 'filtration', '.']
        stop_word = StopWord('some text')
        stop_word.clean = MagicMock(return_value=cleaned)
        removed_stop_words = ['This', 'sample', 'sentence', 'showing', 'stop', 'words', 'filtration']
        self.assertEqual(stop_word.remove(), removed_stop_words)


if __name__ == '__main__':
    unittest.main()
