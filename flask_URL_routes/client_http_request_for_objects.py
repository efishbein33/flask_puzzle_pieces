from flask import Flask, request
app = Flask(__name__)

'''
any request made by the client is passed through a flask object.
showing how the handler functions work to represent the request made by the client
and return the correct response needed.
'''

@app.route('/')
def requestdata():
    ''' prints the IP address and uder agent of the client '''
    return f'''Hello! <br><br> <b> Your IP address is:</b>
            {request.remote_addr} <br> <b> And you are using:</b> {request.user_agent}.'''