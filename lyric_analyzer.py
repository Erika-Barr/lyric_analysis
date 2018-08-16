from stop_words import StopWord
from news_client import NewsClient
import pdb

class LyricAnalyzer(object):
    def __init__(self, lyrics, num):
        '''Returns a top article for each of the top n words.

        Args:
            lyrics (str): Song lyrics inputed from user.
            num (int): Sets the number of top words.
        '''
        self.lyrics = lyrics
        self.num = num
        self.cleaned = StopWord(self.lyrics).remove()


    def top_words(self):
        '''Returns top n words with number of occurences and frequency percentage out of non-stop words.'''
        words = self.cleaned
        word_counter = {}
        wlen = len(words)
        for word in words:
            w = word.lower()
            if word_counter.get(w, 0) == 0:
                word_counter[w] = 1
            else:
                word_counter[w] += 1

        '''*TODO handle if num is more than size of word list'''
        top = list(word_counter.items())[0:self.num]
        formatted_output = {}
        for w in top:
            formatted_output[w[0]] = [w[1], round(w[1]/wlen, 2)]
        return formatted_output




#'''Usage

lyr = "Bag bag bag bag bag run run run run pen pen pen pen science history grammar bottles cars."
l_a = LyricAnalyzer(lyr, 3)

print(l_a.top_words())
#'''
