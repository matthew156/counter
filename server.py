from typing import Counter
from flask import Flask, render_template, redirect, session
app= Flask(__name__)
app.secret_key = 'shh secret'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=1
    return redirect("/")

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
