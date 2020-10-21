class News_article:
    '''
    News_article class to define News_article objects
    '''

    def __init__(self,source, author, title, url, description, urlToImage, publishedAt, content):
        self.source = source
        self.author = author
        self.title = title
        self.url = url
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class News_source:
    '''
    News_source class to define News_source objects
    '''

    def __init__(self,url, description, category, language, country):
        self.url = url
        self.description = description
        self.category = category
        self.language = language
        self.country = country

 
#  Create method that appends the review object to a class variable all _reviews that's an empty list.
    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()