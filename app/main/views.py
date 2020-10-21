from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news_article,get_news_source,search_news_article
from .forms import ReviewForm
from newsapi import NewsApiClient


#Views
#Convert news_id into an integer.
# Create search() that passes in a dynamic variable.
@main.route('/')
def index():
    # form = ReviewForm()
    # news_article = get_news_article(url)

    # if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(source, author, title,description, url,urlToImage, publishedAt, news_article.poster,review)
        new_review.save_review()
        return redirect(url_for('news_article',id = movie.id ))

    '''
    View root page function that returns the index page and its data
    '''

    # Getting trending news_article
    trending_news = get_news_article('trending')
    developing_news = get_news_article('developing')
    now_showing_news = get_news_article('now_playing')
    
    title = 'Home - Best News Website online. '
    
    search_news_article = request.args.get('news_article_query')
    
    if search_news_article:
        return redirect(url_for('search', news_article_title=search_news_article))
    else:
        return render_template('index.html', title = title, trending = trending_news, developing = developing_news, now_playing = now_showing_news)

    return render_template('search.html', news_articles = searched_news_article)