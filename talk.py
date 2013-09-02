from flask import Flask, url_for, render_template, json
from models import Post, Topic
from settings import Session

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/api/posts/")
def posts():
    session = Session()
    topics = session.query(Topic).all()

    a = [{'title': t.title, 'posts': [{'body': p.body} for p in t.posts]} for t in topics]
    return json.dumps(a)

if __name__ == "__main__":
    app.run(debug=True)

