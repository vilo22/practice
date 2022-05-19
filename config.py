#we set up and organized application file structures and configuration here 

#What secret variables does the app need

#and where is the base directory/root folder of the project 

# we're gonna nned a little help from the os package
import os 

basedir =  os.path.abspath(os.path.dirname(__name__))

class Config:
    """
    setting configuration variables that ell our flask app how to run 
    """

    FLASK_APP = os.environ.get('FLASK_APP') #Go get the flask app variable valur from the .env file
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY =os.environ.get('SECRET_KEY')