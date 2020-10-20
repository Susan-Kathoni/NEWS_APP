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