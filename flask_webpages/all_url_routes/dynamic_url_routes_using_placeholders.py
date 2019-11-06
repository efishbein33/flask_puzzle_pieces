from flask import Flask
app = Flask(__name__)

'''
we are creating a dynamic URL that is using a single URL pattern that can recognize a potentially
infinite number of URLs that share the same basic pattern such as /user/<id_number>/ 
'''

@app.route('/user/<id>/')
def user_profile(id):
    return f"Profile page of user #{id}"

# dynamic URL with a single URL pattern that is specific to only integers as inputs
@app.route('/users/<int:id>/')
def user_int_only_profile(id):
    return f"Profile page of user integer only #{id}"