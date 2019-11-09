from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/testpage')
def testpage():
    return render_template('testpage.html')

@app.route('/conditionaleg')
def conditionaleg():
    title = 'This is a test title'
    return render_template('conditionaleg.html', title=title)

@app.route('/testloop')
def testloop():
    posts = [
        {'title': 'Test post 1'},
        {'title': 'Test post 2'},
        {'title': 'Test post 3'}
    ]
    return render_template('testloop.html', title='Posts', posts=posts)
