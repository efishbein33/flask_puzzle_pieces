from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    ''' returns the index template, which includes the navbar template '''
    return render_template('child.html')