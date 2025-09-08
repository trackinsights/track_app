from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Create SQLAlchemy instance **after app**
db = SQLAlchemy(app)

# Import models and queries here (after db is created)
from models import School
from queries import query_example

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/query1")
def query1():
    results = query_example()
    return render_template("query1.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
