<<<<<<< HEAD
# basic_routes_into_web_app.py

''' 
demonstrates how to define route handlers 



create 3 basic URLs:
=======
# basic_routes_into_web_apps.py

'''demonstrates how to define route handlers

create 3 basic URLs: 
>>>>>>> d4b40ebaae67f60b2fcea79f7c2f7365d71c3a56
1: home page
2: career page
3: feedback page

<<<<<<< HEAD
run flask in bash and check all URLs to make sure they all work properly
'''

##__imports__##
from flask import Flask

# use Flask object to run the server and manage configurations in app.config
app = Flask(__name__)

##__thre basic routes with a URL pattern and a handler function__##

=======
run flask in bash and check all URLs to make sure they all work properly.
'''

##___imports___##
from flask import Flask

# use Flask object to run the server and manage configurations in app.config
app = Flask(__name__) 

##___three basic routes with a URL pattern and a handler function___##
>>>>>>> d4b40ebaae67f60b2fcea79f7c2f7365d71c3a56
@app.route('/')
def index():
    return 'Home Page'

@app.route('/career/')
def career():
    return 'Career Page'

@app.route('/feedback/')
def feedback():
    return 'Feedback Page'

