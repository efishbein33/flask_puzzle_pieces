from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.debug = True
app.config['SECRET_KEY'] = 'a really weird and long key in the form of a string'

# store the db connection information in the app.config dictionary under the key 'SQLALCHEMY_DATABASE_URI'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:pass@localhost/flask_app_db'

# initialize an SQLAlchemy object by passing it a Flask object
db = SQLAlchemy(app)

# a model to define a table in a database
class Post(db.Model):
    __tablename__ = 'flask puzzle pieces'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        ''' used to see a string representation of one row of the table '''
        return f"<{self.id}:{self.title[:10]}>"