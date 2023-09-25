from flask import Flask, render_template, request
from forms import SignupForm

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
baseDir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'AMERICA'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(baseDir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
import models

@app.route('/home/<username>')
def main(username):
    to_do_list = [
        {
            'name': 'Buy milk',
            'description': 'Buy 2 liters of milk in Coopmart'
        },
        {
            'name': 'Get money',
            'description': 'Get 500k from ATM'
        },
        {
            'name': 'America',
            'description': 'Make America great again!'
        }
    ]
    return render_template('index.html', to_do_list = to_do_list, request = request, username = username)

@app.route('/', methods = ['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data
        confirm_password = form.confirm_password.data
        
        user = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password,
            'confirm_password': confirm_password
        }
        return render_template('signup_success.html', user = user, request = request)
    return render_template('signup.html', request = request, form = form)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8080)