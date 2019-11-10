from flask import Flask, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a really weird and long key in the form of a string'

@app.route('/session/')
def updating_session():
    ''' demonstrates how to modify a session object '''
    # obtain a string representation of the session key-value pairs which will be returned to the client
    res = str( session.items() )
    
    # We will store this dictionary in the session to represent a baby version of a cart
    cart_items = {'pineapples': '10', 'apples': '20', 'mangos': '30'}
    
    # this will only be true after the URL has been hit once
    if 'cart_items' in session:
       
        # modify one of the key-value pairs in the dictionary that lives in the session
        session['cart_items']['pineapples'] = '100'
        
        # send the updated session cookie to the client
        session.modified = True
    
    else:
        
        # the first time the URL is hit, set the cart to the dictionary line 14
        session['cart_items'] = cart_items
    
    # return a string representation of the cart to the client
    return res