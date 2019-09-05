from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/faceinfo')
def faceinfo():
    return render_template('output.html')