from estudo import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    context ={
        'usuario': 'Usuario',
        'idade': 25,
    }
    return render_template('index.html', context=context)

@app.route('/nova/')
def newpage():
    return 'outra view'