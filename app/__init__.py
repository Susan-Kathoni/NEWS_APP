from flask import Flask

#Initializing application
app = Flask(__name__)

#Import views file in order to create views
from app import views