
from flask import Flask, render_template, request
import os
import sqlite3

app = Flask(__name__)


@app.route('/')
@app.route('/history.html')
def serv():
    return render_template('history.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')