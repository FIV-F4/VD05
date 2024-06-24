from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def ind():
    context = {
        "caption": "Привет, мир!",
        "user": "nina",
        "number": 3,
        "posts": ["пост 1", "пост 2", "пост 3"],
        "menu": 1
    }
    return render_template('home.html', **context)


@app.route('/about')
def ind2():
    context = {
        "caption": "Привет, мир!",
        "user": "nina",
        "number": 3,
        "posts": ["пост 1", "пост 2", "пост 3"],
        "menu": 2
    }
    return render_template('about.html', **context)





if __name__ == '__main__':
    app.run()
