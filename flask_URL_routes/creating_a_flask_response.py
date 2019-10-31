from flask import Flask, make_response, redirect
app = Flask(__name__)

'''
3 ways to create a reponse with Flask
    1. As a strong or using a template engine. 
    2. As a response object. 
    3. As a tuple in the form(reponse, status, headers) or (response, headers).
'''

'''
1.
creating a response object manually using the make_reponse function.
Flask automatically converts a string into a reponse object when it is put
through a view function and we use the make_response function

we've used this method in file: putting_all_url_routes_together.py

@app.route('/books/<genre>')
def books(genre):
    return f"All Books in {genre} category"
'''
 
'''
2.
We are creating a manual response using the syntax 'make_response()' function.
response=make_reponse(res_body, status_code=200)
We are doing this to manually craft a reponse rather than relying on the default behavior of Flask
'''
# a route with a dynamic URL pattern
@app.route('/books/<genre>')
def books(genre):
    # create a response object whose body is a string
    response_string = f"All Books in {genre} category"
    response = make_response(response_string)
    response.headers['Content-Type'] = 'text/plain'
    response.headers['Server'] = 'Foobar'
    return response

# a route with a dynamic URL that returns a 404 error
@app.route('/')
def handler_that_returns_a_404_error():
    return make_response("<h2>404 Error</h2>", 400)

'''
3.
We are creating a response object using one of the following tuple formats:
    1. (response, status, headers)
    2. (response, headers)
    3. (response, status)
response = string that is the body of the response
status = HTTP status code
headers = dictionary of values
'''

'''
we are creating a redirect URL by using the redirect function that flask provides us.
'''

# a route that redirects the client to the URL for the login page

@app.route('/redirect/')
def transfer():
   # return '', 302, {'location': 'http://localhost:5000/login'} -- no longer necessary
   return redirect('http://localhost:5000/login')

# the login page

@app.route('/login/')
def say_hello():
    return 'Welcome to the login page!'