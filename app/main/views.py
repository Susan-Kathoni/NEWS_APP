from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news_sources,get_source_articles
# from .forms import ReviewForm
# from ..models import Review
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data.
    '''
    
    business = get_news_sources('business')
    technology = get_news_sources('technology')
    sports = get_news_sources('sports')
    entertainment = get_news_sources('entertainment')
    
    title = 'Home -  Daily News'
    search_news = request.args.get('news_query')
    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title, business_sources = business, technology_sources = technology,sports_sources = sports,  entertainment_sources = entertainment)


@main.route('/sources/<id>')
def articles(id):
    '''
    view articles page
    '''
    articles = get_source_articles(id)
    title = f'NH | {id}'
    return render_template('news.html', title=title, articles=articles)