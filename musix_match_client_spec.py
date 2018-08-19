from musix_match_client import MusixMatchClient
import unittest
from unittest.mock import MagicMock
import pdb

class TestMusixMatchClient(unittest.TestCase):
    def test_get_lyrics(self):
        api = MusixMatchClient('artist_name', 'song_name')
        response = {"message": {"body": {"lyrics": {"lyrics_body": "some lyrics for external api"}}}}
        #stub external api function
        api.external_api.matcher_lyrics_get_get = MagicMock(return_value=response)
        lyrics = "some lyrics for external api"
        self.assertEqual(api.get_lyrics(), lyrics)


if __name__ == '__main__':
    unittest.main()


