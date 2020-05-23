from flask import Flask
from flask import render_template, redirect, url_for, request


app = Flask(__name__)
results = []


@app.route('/123', methods=['GET'])
def Page():
    return render_template('indices.html', results=[])


@app.route('/', methods=['GET', 'Post'])
def test_page1():
    if request.method == 'POST':
        List = request.form['List']
        Number = request.form['Number']
        return '<h1>List is {} . Number is {}.</h1>'.format(List, Number)
    return render_template('indices.html')
