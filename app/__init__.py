from flask import Flask
from .config import DevConfig

#Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

#Import views file in order to create views
from app import views