import datetime

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# CONFIGURE FORMS
class CreatePostForm(FlaskForm):
    title = StringField(label="Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Post Subtitle", validators=[DataRequired()])
    author = StringField(label="Post Author", validators=[DataRequired()])
    img_url = StringField(label="Post Image URL", validators=[DataRequired(), URL()])
    content = CKEditorField(label="Blog Content", validators=[DataRequired()])
    submit = SubmitField(label="Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    requested_post = db.session.get(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=["GET", "POST"])
def create_new_post():
    new_post_form = CreatePostForm()
    if new_post_form.validate_on_submit():
        data = request.form
        new_post = BlogPost(
            title=data["title"],
            subtitle=data["subtitle"],
            date=datetime.now().strftime("%B %d, %Y"),
            body=data["content"],
            author=data["author"],
            img_url=data["img_url"]
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=new_post_form, new_post=True)


@app.route('/edit-post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    post_to_edit = db.get_or_404(BlogPost, post_id)
    edit_form = CreatePostForm(
        title=post_to_edit.title,
        subtitle=post_to_edit.subtitle,
        img_url=post_to_edit.img_url,
        author=post_to_edit.author,
        content=post_to_edit.body
    )
    if edit_form.validate_on_submit():
        data = request.form
        post_to_edit.title = data["title"]
        post_to_edit.subtitle = data["subtitle"]
        post_to_edit.img_url = data["img_url"]
        post_to_edit.author = data["author"]
        post_to_edit.body = data["content"]
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_to_edit.id))
    return render_template("make-post.html", form=edit_form, new_post=False)


@app.route('/delete-post/<int:post_id>')
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
