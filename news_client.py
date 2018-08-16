from newsapi import NewsApiClient
import random
import pdb

class NewsClient(object):
    '''Returns a top article'''
    def __init__(self, keyword):
        '''Initialize API instance
        Args:
            keyword (str): Word to search news.

        '''
        self.news_api = NewsApiClient(api_key='5bd819d333364b0d93ffa981b3a9e541')
        self.keyword = keyword

    def get_top_articles(self):
        '''Returns a list of top articles.'''
        top_articles = self.news_api.get_top_headlines(q=self.keyword, language='en')
        return top_articles

    def random_top_article(self):
        '''Returns a dictionary representing a randomly picked top article.'''
        articles = self.get_top_articles()['articles']
        article_index = random.randint(0, len(articles)-1)
        return articles[article_index]

    def parse_title_and_url(self):
        '''Returns a list with the articles title and url.'''
        article = self.random_top_article()
        #data = {'title': article['title'], 'url': article['url']}
        data = [article['title'], article['url']]
        return data


'''Usage
keyword = 'bitcoin'

api = NewsClient(keyword)

info = api.parse_title_and_url()

print(info)
'''
output = []
words = ['apple', 'orange', 'bag']
#pdb.set_trace()
for w in words:
    d = NewsClient(w).get_top_articles()
    if d['totalResults'] is 0:
        continue
    else:
        output.append(NewsClient(w).parse_title_and_url())

#print(output)
