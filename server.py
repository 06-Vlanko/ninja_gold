from flask import Flask, render_template, redirect, request, session
import random

app = Flask (__name__)
app.secret_key = 'mykey'

@app.route ('/')
def index():
    print session
    if not session:
        session['total_gold']=0
    return render_template('index.html', total_gold=session['total_gold'])

@app.route ('/process_money', methods=['POST'])
def processMoney ():
    session['total_gold'] += 10
    return redirect ('/')

@app.route ('/clear')
def clearing():
    session.clear()
    print session
    return redirect ('/')

app.run(debug=True)