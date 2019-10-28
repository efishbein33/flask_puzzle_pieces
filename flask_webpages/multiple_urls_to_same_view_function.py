from flask import Flask
app = Flask(__name__)

@app.route('/contact/')
@app.route('/feedback/')
def feedback():
    return 'Feedback Page'