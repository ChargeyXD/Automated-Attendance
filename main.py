from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy
import facerec as fc

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/video')
def video():
    return "video"

if __name__ == "__main__":
    app.run(debug=True)
