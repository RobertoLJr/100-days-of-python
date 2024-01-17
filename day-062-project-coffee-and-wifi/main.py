from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, URL
import csv

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


class CafeForm(FlaskForm):
    COFFEE_CHOICES = ["✖️", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
    WIFI_CHOICES = ["✖️", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
    POWER_OUTLET_CHOICES = ["✖️", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]

    cafe = StringField('Cafe name', validators=[DataRequired()])
    url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=COFFEE_CHOICES, validators=[DataRequired()])
    wifi_rating = SelectField("Wi-Fi Strength Rating", choices=WIFI_CHOICES, validators=[DataRequired()])
    power_outlet_rating = SelectField("Power Socket Availability", choices=POWER_OUTLET_CHOICES,
                                      validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        form_data = list(request.form.values())[1:-1]
        print(form_data)
        with open("./cafe-data.csv", "a", encoding="UTF-8") as csv_file:
            csv_file.write(",".join(form_data) + "\n")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
