from flask import Flask
app = Flask(__name__)

'''
mapping two URL's 'contact' and 'feedback' to the same view function of 'Feedback Page'
so that both URL's will take you to the same webpage.
'''

@app.route('/contact/')
@app.route('/feedback/')
def feedback():
    return 'Feedback Page'