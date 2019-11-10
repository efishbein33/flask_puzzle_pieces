from flask import Flask, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a really weird and long key in the form of a string'

@app.route('/visits-counter/')
def visits():
    ''' count how many times the client has hit the endpoint /visits-counter '''
    # if the session has a key named 'visits' then add 1 to whatever the value is
    if 'visits' in session:
        # updates session data
        session['visits'] = session.get('visits') + 1
    # otherwise, this is the first time the client has hit this endpoint - initialize to 1
    else:
        # set session data
        session['visits'] = 1

    # either way, return the total number of visits in a string
    total_number_of_visits = session.get('visits')
    return f"Total visits: {total_number_of_visits}"


@app.route('/delete-visits/')
def delete_visits():
    ''' delete the information from the session dictionary relating to frequency of visits '''
    # delete visits by popping it off of the data structure
    session.pop('visits', None)
    # confirm that the delete was successful
    return 'Visits deleted'