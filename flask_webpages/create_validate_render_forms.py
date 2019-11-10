from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from forms import ContactForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a really weird and long key in the form of a string'

@app.route('/contact/', methods=['get', 'post'])
def contact():
    ''' create a handler function for a contact page'''
    # instantiate a Form object. If a GET request was received, then we will pass the object
    # to a template for further processing. If a POST request was received, then WTForms automatically
    # initializes the form with the data that was entered by the user. We capture the data in this case.
    
    form = ContactForm()

    # if the form is valid then a POST request must have been issued with the form data.
    # capture all of the submitted information into Python variables for further processing.

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message = form.message.data

        # print the information in the console to make sure it was captured properly
        print(name)
        print(email)
        print(message)

        #__db logic goes here__#

        # redirect to the same page with a GET request
        return redirect(url_for('contact'))

    return render_template('contact.html', form=form)