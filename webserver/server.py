from flask import Flask,render_template
import os

app = Flask(__name__)


@app.route('/')
def Todo():
    return render_template('index.html')






if __name__ == '__main__':
    app.run(debug = True)