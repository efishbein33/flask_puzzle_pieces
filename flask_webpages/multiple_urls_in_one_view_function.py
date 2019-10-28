from flask import Flask
app = Flask(__name__)

# mapped both URL's 'contact' and 'feedback' to the same view function of 'Feedback Page'
@app.route('/contact/')
@app.route('/feedback/')
def feedback():
    return 'Feedback Page'