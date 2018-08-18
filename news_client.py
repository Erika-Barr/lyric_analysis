from newsapi import NewsApiClient
import random
import os
import pdb

class NewsClient(object):
    '''Returns a top article'''
    def __init__(self, keyword):
        '''Initialize API instance
        Args:
            keyword (str): Word to search news.

        '''
        self.news_api = NewsApiClient(api_key=os.environ['NEWS_API'])
        self.keyword = keyword

    #Tested in current corresponding spec
    def get_top_articles(self):
        '''Returns a list of top articles.'''
        top_articles = self.news_api.get_top_headlines(q=self.keyword, language='en')
        if top_articles['totalResults'] is 0: return None
        return top_articles

    #Tested in current corresponding spec
    def random_top_article(self):
        '''Returns a dictionary representing a randomly picked top article.'''
        find_articles = self.get_top_articles()
        if find_articles is None: return None
        articles = find_articles['articles']
        article_index = random.randint(0, len(articles)-1)
        return articles[article_index]

    #Tested in current corresponding spec
    def parse_title_and_url(self):
        '''Returns a list with the articles title and url.'''
        article = self.random_top_article()
        if article is None: return None
        data = [article['title'], article['url']]
        return data



'''Usage
keyword = 'bitcoin'

api = NewsClient(keyword)

info = api.parse_title_and_url()

print(info)
output = []
#words = ['jizzi', 'apple', 'orange', 'bag']
words = ['jizzi', 'orange', 'bag']
for w in words:
    output.append(NewsClient(w).parse_title_and_url())

print(output)
'''
