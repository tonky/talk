from flask import Flask, url_for, render_template, json

app = Flask(__name__)

# url_for('static', filename='js/angular.js')

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/api/posts/")
def posts():
    return json.dumps([{'title': 'my first post'}, {'title': 'second post'}])


if __name__ == "__main__":
    app.run(debug=True)

