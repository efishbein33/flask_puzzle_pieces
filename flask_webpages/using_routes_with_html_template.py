from flask import Flask, render_template
app = Flask(__name__)

'''
we are creating our URL route that is working together with our html template to be able
to create an infinite amount of web pages and links without having to create each one
in its own view function.
'''

@app.route('/')
def index():
    # define three variable
    name, age, profession = "Jerry", 24, 'Programmer'

    # prepare a dictionary of these variable to pass to the template
    template_context = dict(name=name, age=age, profession=profession)
    return render_template('index.html', **template_context)