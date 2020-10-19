from flask import render_template
#Import app instance from app folder
from app import app

#Views
#Convert news_id into an integer.
@app.route('/news/<int:news_id>')
def index():

    '''
    View news page function that returns news details page and its data
    '''

    title = 'Home - Welcome to The best News Website Online'
    #Add message variable.
    #Replace message variable with movie_id.
    #Create a variable title and pass it to templates.
    return render_template('news.html',title = title)