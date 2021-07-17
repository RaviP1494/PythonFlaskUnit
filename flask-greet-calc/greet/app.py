from flask import Flask

app = Flask(__name__)


@app.route('/welcome')
def welcome():
    """Basic page returning 'welcome'"""
    return 'welcome'


@app.route('/welcome/home')
def welcome_home():
    """Basic page returning 'welcome home'"""
    return 'welcome home'


@app.route('/welcome/back')
def welcome_back():
    """Basic page returning 'welcome back'"""
    return 'welcome back'