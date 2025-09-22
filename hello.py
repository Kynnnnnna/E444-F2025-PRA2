from flask import Flask, render_template
from datetime import datetime
from flask_moment import Moment
from flask_bootstrap import Bootstrap

app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('index.html', name=name, current_time=datetime.utcnow())

if __name__ == '__main__':
    app.run(debug=True)