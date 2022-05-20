from flask import Flask

from config import Config

app = Flask(__name__)

#here you start to configure bro 

app.config.from_object(Config)

from . import routes #aka from the app folder(this folder), import the entire routes file 
