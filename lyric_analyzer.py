from stop_words import StopWord
from news_client import NewsClient
import pdb

class LyricAnalyzer(object):
    def __init__(self, lyrics, num=3):
        '''Returns a top article for each of the top n words.

        Args:
            lyrics (str): Song lyrics inputed from user.
            num (int): Sets the number of top words.
        '''
        self.lyrics = lyrics
        self.num = num


    #Tested in stop_word_spec
    def clean(self):
        return StopWord(self.lyrics).remove()

    #Tested in current corresponding spec
    def top_words(self):
        '''Returns top n words with number of occurences and frequency percentage out of non-stop words.'''
        words = self.clean()
        word_counter = {}
        wlen = len(words)
        for word in words:
            w = word.lower()
            if word_counter.get(w, 0) == 0:
                word_counter[w] = 1
            else:
                word_counter[w] += 1

        '''*TODO handle if num is more than size of word list
        solution: if num > size then set num to size of word list
        '''
        top = list(word_counter.items())[0:self.num]
        formatted_output = {}
        for w in top:
            formatted_output[w[0]] = [w[1], round(w[1]/wlen, 2)]
        return formatted_output

    #Tested in news_client_spec
    def title_and_url(self, w):
        return NewsClient(w).parse_title_and_url()

    #Not Tested
    def get_info(self,words):
        top = words
        for word in top:
            #Trouble mocking function in for loop
            info = self.title_and_url(word)
            if info is None: continue
            for i in info:
                top[word].append(i)
        return top

    #Tested in current corresponding spec
    def top_articles(self):
        '''Returns a list of formatted dictionaries { word: { occurences, percentage, title, url} }'''
        keys = ['occurences', 'percentages', 'title', 'url']
        words = self.top_words()
        word_info = self.get_info(words)
        data = {}
        for word in word_info:
            data[word] = dict(zip(keys,word_info[word]))
        return data




#print(l_a.top_words())
#lyr = "Bag bag bag bag bag run run run run pen pen pen pen science history grammar bottles cars."
#l_a = LyricAnalyzer(lyr, 3)
#print(l_a.top_articles())
