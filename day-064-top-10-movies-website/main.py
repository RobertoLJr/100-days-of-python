import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# Create DB
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Create table
class Movie(db.Model):
    id: Mapped[str] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# Forms
class EditForm(FlaskForm):
    rating = FloatField("Your Rating Out of 10 (e.g. 7.5)", validators=[DataRequired(), NumberRange(0, 10)])
    review = StringField("Your Review")
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        parameters = {
            "query": form.title.data
        }

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {os.getenv('TMDB_TOKEN')}"
        }

        response = requests.get("https://api.themoviedb.org/3/search/movie", headers=headers, params=parameters)
        response.raise_for_status()
        data = response.json()["results"]

        return render_template("select.html", movies=data)
    return render_template("add.html", form=form)


@app.route("/find")
def find():
    movie_id = request.args.get("id")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_TOKEN')}"
    }

    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}", headers=headers)
    response.raise_for_status()
    data = response.json()
    new_movie = Movie(
        title=data["original_title"],
        year=data["release_date"][:4],
        description=data["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id=new_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    movie_to_edit = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie_to_edit.rating = float(form.rating.data)
        movie_to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", form=form, movie=movie_to_edit)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
