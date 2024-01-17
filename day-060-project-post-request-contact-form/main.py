from flask import Flask, render_template, request
import os
import requests
import smtplib

OWN_EMAIL = os.environ.get("OWN_EMAIL")
OWN_PASSWORD = os.environ.get("OWN_PASSWORD")

app = Flask(__name__)

response = requests.get('https://api.npoint.io/3211c5c50d1e05e054a0')
response.raise_for_status()
data = response.json()


@app.route('/')
def home():
    return render_template("index.html", posts=data)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        form_data = request.form
        send_email(form_data["name"], form_data["email"], form_data["phone"], form_data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    with smtplib.SMTP(f"smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=OWN_EMAIL, password=OWN_PASSWORD)
        connection.sendmail(
            from_addr=OWN_EMAIL,
            to_addrs=OWN_EMAIL,
            msg=f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
        )


@app.route('/<int:index>')
def get_post(index):
    requested_post = None
    for post in data:
        if post["id"] == index:
            requested_post = post

    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
