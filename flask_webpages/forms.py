''' create forms using Library Flask-WTForm.
using python code Flask will write out all our
html code for us depending on what class objects 
we use that's built into our Library. '''

# our forms will inherit from this class definition
from flask_wtf import FlaskForm

# our fields will be objects of these types
from wtforms import StringField, SubmitField, TextAreaField

# code that lets us validate our forms easily
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    ''' define a contact form by inheriting from the FlaskForm class '''
    
    # name field expects a string
    name = StringField("Name: ", validators=[DataRequired()])

    # email field expects a string
    email = StringField("Email: ", validators=[Email()])

    # message field expects a text area
    message = TextAreaField("Message", validators=[DataRequired()])

    # represents an <input type="submit"> HTML element
    submit = SubmitField("Submit")
