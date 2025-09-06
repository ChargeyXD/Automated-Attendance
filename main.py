from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import facerec as fc

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello there"

@app.route('/video')
def camera_feed():
    return fc.Webcam()

if __name__ == "__main__":
    app.run(debug=True)
