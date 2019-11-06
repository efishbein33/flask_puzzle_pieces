from flask import Flask
app = Flask(__name__)

''' This decorator registers a function to execute before the first request is handled. '''
@app.before_first_request
def before_first_request():
    print("before_first_request() called")

''' This decorator registers a function to execute before a request is handled. '''
@app.before_request
def before_request():
    print("before_request() called")

'''
This decorator registers a function to execute after a request is handled.
The registered function will not be called in case an unhandled exception occurred in the
request handler. The function must accept a response object and return the same or new
response.
'''
@app.after_request
def after_request(response):
    print("after_request() called")
    return response

'''
teardown_request: Similar to after_request decorator but the registered function will
always execute regardless of whether the request handler throws an exception or not.
'''
@app.route("/")
def index():
    print("index() called")
    return '<p>Testing Request Hooks</p>'
