from flask import Flask
from .config import DevConfig

# Initializing application.
# Add instance_relative_config to connect to instance folder when creating app instance.
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
# Connect to the config file and append its contents to app.config
app.config.from_pyfile('config.py')

# Import views file in order to create views
from app import views