from flask import Flask
app = Flask(__name__)

'''
creating one page of the different types of URL style pages we have created thus far
1. basic route with a URL pattern and a handler function
2. route that uses a dynamic URL pattern
3. dynamic URL pattern with no converter
'''

# basic route
@app.route('/')
def index():
    return 'Hello Flask'

# dynamic URL pattern with integer only
@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return f"Profile page of user #{user_id}"

# dynamic URL pattern with no converter
@app.route('/books/<genre>/')
def books(genre):
    return f"All books in {genre} category"