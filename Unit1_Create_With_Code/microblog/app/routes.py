from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Fletcher'}
    posts = [
        {
            'author': {'username': 'Fred'},
            'body': 'Basketball is the best sport!'
        }
    ]
    return render_template('index.html', title=user['username'], user=user, posts=posts)
