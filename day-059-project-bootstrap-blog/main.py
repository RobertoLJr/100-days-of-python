from flask import Flask, render_template
import requests

app = Flask(__name__)


response = requests.get('https://api.npoint.io/3211c5c50d1e05e054a0')
response.raise_for_status()
data = response.json()
print(data)


@app.route('/')
def home():
    return render_template("index.html", posts=data)


@app.route('/about')
def about():
    return render_template("about.html")



@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/<int:index>')
def get_post(index):
    requested_post = None
    for post in data:
        if post["id"] == index:
            requested_post = post

    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
