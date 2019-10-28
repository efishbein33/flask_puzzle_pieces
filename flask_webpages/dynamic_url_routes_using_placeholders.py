from flask import Flask
app = Flask(__name__)

'''
we are creating a dynamic URL that is using a single URL pattern that can recognize a potentially
infinite number of URLs that share the same basic pattern such as /user/<id_number>/ 
'''

@app.route('/user/<id>/')
def user_profile(id):
    return f"Profile page of user #{id}"