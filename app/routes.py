from app import app
from flask import render_template, render_template_string

link_strings = {
    'homepage': 'index',
    'about me': 'about',
    'basic joins': 'basicjoins',
    'basic matplotlib scatter': 'matplotlib-scatter',
    'pd read csv methods': 'pdreadcsv',
    'basic vlookups':'vlookups'
}


@app.route('/')
@app.route('/'+link_strings['homepage'])
def index():
    pp = link_strings['homepage']
    return render_template(pp+'.html', path=pp, preview_list=link_strings)


@app.route('/'+link_strings['basic joins'])
def basicjoins():
    pp = link_strings['basic joins']
    return render_template(pp+'.html', path=pp)


@app.route('/'+link_strings['basic matplotlib scatter'])
def plt_scatter():
    pp = link_strings['basic matplotlib scatter']
    pdcsv_link = '/'+ link_strings['pd read csv methods']
    return render_template(pp+'.html', path=pp, pdcsv_link=pdcsv_link)


@app.route('/'+link_strings['basic vlookups'])
def vlookups():
    pp=link_strings['basic vlookups']
    return render_template(pp+'.html', path=pp)


@app.route('/'+link_strings['pd read csv methods'])
def pd_read_csv():
    pp=link_strings['pd read csv methods']
    return render_template(pp+'.html', path=pp)



# Test pages
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

