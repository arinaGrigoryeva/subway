from flask import Flask, render_template, request
import os
import sqlite3

app = Flask(__name__)


@app.route('/')
@app.route('/index_new.html')
def serv():
    return render_template('index_new.html')


@app.route('/history.html')
def history():
    return render_template('history.html')


@app.route('/stations.html')
def stations():
    return render_template('stations.html')


@app.route('/trains.html')
def trains():
    return render_template('trains.html')


@app.route('/facts.html')
def facts():
    return render_template('facts.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/otz.html', methods=['POST', 'GET'])
def otz():
    if request.method == 'GET':
        return render_template('otz.html')
    elif request.method == 'POST':
        name = request.form['email']
        score = request.form['about']
        conn = sqlite3.connect('ag.db')
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS ag(names TEXT, '
                  'scores TEXT)')

        c.execute('INSERT INTO ag(names, scores) VALUES (?, ?)', (name, score))
        c.execute("SELECT names FROM ag")
        rez = c.fetchall()
        conn.commit()
        c = conn.cursor()
        c.execute("SELECT scores FROM ag")
        rezz = c.fetchall()
        v = str(rezz)
        t = v.replace('(', " ")
        n = t.replace(')', " ")
        r = n.replace(', ,', ",")
        conn.commit()

        # return v[1:-1]
        return oxc(r)


@app.route('/oxc.html')
def oxc(r):
    return render_template('oxc.html', table=r[1:-1])


if __name__ == '__main__':
    #port = int(os.environ.get("PORT", 22))
    app.run(host='185.50.25.11', port=22)