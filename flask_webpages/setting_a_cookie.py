from flask import Flask, make_response, request

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a really weird and long key in the form of a string'

@app.route('/cookie/')
def cookie():
    ''' demonstrates how to set a cookie in the client '''
    # if the cookie with key 'foo' has not yet been set in the client, then set it now
    if not request.cookies.get('foo'):    
        response_object = make_response("Setting a cookie")

        # create a cookie named 'foo' with the value 'bar' that will last for 2 years (number of seconds in a year).
        response_object.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    
    # otherwise, the cookie was already set and we can extract it from the request
    else:
        # get the cookie value corresponding to the key 'foo'
        cookie_value = request.cookies.get('foo')
        response_object = make_response(f"The client sent a cookie whose value is {cookie_value}!")

    # return whichever response object ended up being created
    return response_object