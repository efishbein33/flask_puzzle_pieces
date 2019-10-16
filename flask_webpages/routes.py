from flask import Flask
app = Flask(__name__)

# a route with a dynamic URL pattern
@app.route('/books/<genre>')
def books(genre):
    # create a response object whose body is a string
    response_string = f"All Books in {genre} category"
    response = make_response(response_string)
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Server'] = 'Foobar'
    return response


# a route that redirects to the client to the URL login page
@app.route('/redirect/')
def transfer():
   # return '', 302, {'location': 'http://localhost:5000/login'} -- no longer necessary
    return redirect('http://localhost:5000/login')

# the login page
@app.route('/login/')
def say_hello():
    return 'Welcome to the login page!'

''' # basic route with a URL pattern and a handler function
@app.route('/')
def index():
    return 'Hello Flask' 
'''
# route that uses a dynamic URL pattern
@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return f"Profile page of user #{user_id}"

''' # another route that uses a dynamic URL pattern but does not use a converter
@app.route('/books/<genre>/')
def books(genre):
    return f"All Books in {genre} category"
'''

@app.before_first_request
def before_first_request():
    print("before_first_request() called")

@app.before_request
def before_request():
    print("before_request() called")

@app.after_request
def after_request(response):
    print("after_request() called")
    return response

@app.route("/")
def index():
    print("index() called")
    return '<p>Testings Request Hooks</p>'