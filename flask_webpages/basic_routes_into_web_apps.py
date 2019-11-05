# basic_routes_into_web_app.py

''' 
demonstrates how to define route handlers 



create 3 basic URLs:
1: home page
2: career page
3: feedback page

run flask in bash and check all URLs to make sure they all work properly
'''

##__imports__##
from flask import Flask

# use Flask object to run the server and manage configurations in app.config
app = Flask(__name__)

##__thre basic routes with a URL pattern and a handler function__##

@app.route('/')
def index():
    return 'Home Page'

@app.route('/career/')
def career():
    return 'Career Page'

@app.route('/feedback/')
def feedback():
    return 'Feedback Page'

