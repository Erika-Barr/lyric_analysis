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
        '''Returns a dictionary with the articles title and url.'''
        article = self.random_top_article()
        data = {'title': article['title'], 'url': article['url']}
        return data


'''Usage
keyword = 'bitcoin'

api = NewsClient(keyword)

info = api.parse_title_and_url()

print(info)
'''
