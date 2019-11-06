from flask import Flask, render_template
app = Flask(__name__)

@app.route('/admin/')
def admin():
    # if not logged in then redirect the user to the login page
    if not loggedin:
        return redirect(url_for('login'))
    return render_template('admin.html')