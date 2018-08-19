from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class StopWord(object):
    '''Return a list of words excluding stop words.'''
    def __init__(self, text):
        '''Args:
            text (str): Lyrics from user.'''
        self.text = text

    #Tested in current corresponding spec
    def clean(self):
        '''Returns list of tokenized words.'''
        return word_tokenize(self.text)

    #Tested in current corresponding spec
    def remove(self):
        '''Returns list excluding stop words and non-alphabetical characters.'''
        words = self.clean()
        removed = []
        stop_words = set(stopwords.words('english'))
        for word in words:
            if word.lower() not in stop_words and word.isalpha():
                removed.append(word)
        return removed

'''Usage
s = StopWord('This is a sample sentence, showing off the stop words filtration.')
rem = s.remove()
print(rem)
'''
