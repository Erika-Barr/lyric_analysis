import pdb
import os
import swagger_client
from swagger_client.rest import ApiException

class MusixMatchClient(object):
    '''Returns client for Musixmatch api'''
    def __init__(self, artist, track):
        '''Initialize external API instance.
        Args:
            artist (str): Artist name.
            track (str): Track name.
        '''
        swagger_client.configuration.api_key['apikey'] = os.environ['MUSIX_MATCH_KEY']
        self.external_api = swagger_client.LyricsApi()
        self.artist = artist
        self.track = track

    def get_lyrics(self):
        '''Returns lyrics from Musixmatch api'''
        kwargs = {"q_track": self.track, "q_artist": self.artist}
        response = self.external_api.matcher_lyrics_get_get(**kwargs)
        #lyrics = response["message"]["body"]["lyrics"]["lyrics_body"]
        lyrics = response.message.body.lyrics.lyrics_body
        return lyrics

l = MusixMatchClient('XXXTentacia', 'Moonlight')
print(l.get_lyrics())
