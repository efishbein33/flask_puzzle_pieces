from flask import Flask, request
app = Flask(__name__)

# basic route with a URL pattern and a handler function
''' @app.route('/')
def index():
    return 'Hello Flask' '''

# route that uses a dynamic URL pattern
@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return f"Profile page of user #{user_id}"

# another route that uses a dynamic URL pattern but does not use a converter
@app.route('/books/<genre>/')
def books(genre):
    return f"All Books in {genre} category"

@app.route('/')
def requestdata():
    ''' prints the ip address and user agent of the client '''
    return f'''Hello! <br><br> <b> Your IP address is:<b>
                {request.remote_addr} <br>  <b>And you are using:</b> {request.user_agent}.'''