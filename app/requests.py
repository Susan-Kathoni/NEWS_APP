from app import app
import urllib.request,json
from .models import News_article

# Getting api key
api_key = None
# Getting news_article base url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']


def get_news_article(source):
    '''
    Function that gets the json response to our url request
    '''
    get_news_article_url = base_url.format(source,api_key)


    with urllib.request.urlopen(get_news_article_url) as url:
        news_article_data = url.read()
        news_article_response = json.loads(news_article_data)

        news_article_object = None
        if news_article_response['article']
            news_article_list = get_news_article news_article_details_response
            news_article_results = process_results(news_article_results_list)
            
    return news_article_result


# Function that takes in a list of dictionaries
def process_results(news_article_list):
    '''
    Function that processes the news_article result and transform them to a list of Objects

    Args:
        news_article_list: A list of dictionaries that contain news_article details

    Returns :
        news_article: A list of news_article objects
    '''

    # Create empty list to store newly created news_article objects
    news_article_results = []
    for news_article_item in news_article_list:
        source = news_article_item.get('source')
        author = news_article_item.get('author')
        title  = news_article_item.get('title')
        url    = news_article_item.get('url')
        description = news_article_item.get('description')
        urlToImage  = news_article_item.get('urlToImage')
        publishedAt = news_article_item.get('publishedAt')
        content     = news_article_item.get('content')

        if image:
            news_article_object = News_article(source, author, title, url, description, urlToImage, publishedAt, content)
            news_article_results.append(news_article_object)

        return news_article_results

def get_news_source(source):
    '''
    Function that gets the json response to our url request
    '''
    get_news_source_url = base_url.format(source,api_key)

    with urllib.request.urlopen(get_news_source_url) as url:
        # Add function to read the response and tie it in get_news_source_data variable
        get_news_source_data = url.read()
        get_news_source_response = json.loads(news_source_data)

        news_source_object = None

    if news_source_response:
        return news_source_results

# Function that takes in a list of dictionaries
def process_results(news_source_list):
    '''
    Function that processes the news_source result and transform them to a list of Objects

    Args:
        news_source_list: A list of dictionaries that contain news_source details

    Returns :
        news_source: A list of news_source objects
    '''

    # Create empty list to store newly created news_source objects
    news_source_results = []
    for news_source_item in news_source_list:
        url    = news_source_item.get('url')
        category = news_source_item.get('category')
        language  = news_source_item.get('language')
        country = news_source_item.get('country')
        

        if poster:
            news_source_object = News_source(url, source, language, country)
            news_source_results.append(news_source_object)

        return news_source_results

# Create search request
def search_news_article(news_article_title):
    search_news_article_url = 'https://newsapi.org/v2/sources/{}?apiKey={}&query={}'.format(api_key,news_article_title)
    with urllib.request.urlopen(search_news_article_url) as url:
        search_news_article_data = url.read()
        search_news_article_response = json.loads(search_news_article_data)

        search_news_article_results = None

        if search_news_article_response['results']:
            search_news_article_list = search_news_article_response['results']
            search_news_article_results = process_results(search_news_article_list)


    return search_news_article_results


    