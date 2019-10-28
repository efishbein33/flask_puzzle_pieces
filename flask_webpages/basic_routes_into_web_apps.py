from flask import Flask
app = Flask(__name__) # we are naming our Flask object 'app' we us @app to define our routes

''' 
creating 3 basic webpages within 1 web app. 
1: home page
2: career page
3: feedback page

run flask in bash and check your URLs to make sure they all work properly
'''
# three basic routes with a URL pattern and a handler function
@app.route('/')
def index():
    return 'Home Page'

@app.route('/career/')
def career():
    return 'Career Page'

@app.route('/feedback/')
def feedback():
    return 'Feedback Page'

