''' create a login page that give the user a form to fill out username and password
after they enter the information, the information is sent to a server,
ultimatelt reaches the view function of our choice. '''

from flask import Flask, render_template, request
app = Flask(__name__)

# handler function for either post or get requests to the url '/login/'
@app.route('/login/', methods=['post', 'get'])
def login():
    # start preparing the return message
    message = ''
    # if information was posted to the URL, then get it and check if it's correct
    if request.method == 'POST':
        # access the data that was submitted into the form
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'root' and password == 'pass':
            message = "Correct username and password!"
        else:
            message = "Wrong username or password :("

    # the template is rendered whether a GET or POST request was sent.
    # the difference is that we display a different message depending upon the request
    return render_template('login.html', message=message)
