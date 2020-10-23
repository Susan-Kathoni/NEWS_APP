class Source:
    """ Sources class to define the news source objects """
    def __init__(self, id, name, description, url, category):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category

class Article:
    """ Articles class to define the articles object """
    def __init__(self, author, title, description, pathToImage, url, datePublished):
        self.author = author
        self.title = title
        self.description = description
        self.pathToImage = pathToImage
        self.url = url
        self.datePublished = datePublished 

    def save_article(self):
        article.all_articles.append(self)


class Review:

    all_reviews = []

    def __init__(self,source,title,urlToImage,review):
        self.source = source
        self.title = title
        self.urlToImage = urlToImage
        self.review = review
 
#  Create method that appends the review object to a class variable all _reviews that's an empty list.
    def save_review(self):
        Review.all_reviews.append(self)


    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()