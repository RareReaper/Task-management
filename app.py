from flask import Flask, redirect, render_template, request, session
from helper import login_required


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
