import random
from flask import Flask

app = Flask(__name__)
NUMBER = random.randint(0, 9)


@app.route("/")
def home():
    return ("<h1>Guess a number between 0 and 9</h1>"
            '<iframe src="https://giphy.com/embed/mlvseq9yvZhba" width="480" height="480" frameBorder="0" '
            'class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/funny-cat-mlvseq9yvZhba">'
            'via GIPHY</a></p>')


@app.route("/<int:guess>")
def guess_number(guess):
    if guess < NUMBER:
        return ("<h1 style='color: red'>Too low, try again!</h1>"
                '<iframe src="https://giphy.com/embed/23eIaihzejUmUtIDkO" width="270" height="480" frameBorder="0" '
                'class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/23eIaihzejUmUtIDkO">'
                'via GIPHY</a></p>')
    elif guess > NUMBER:
        return ("<h1 style='color: purple'>Too high, try again!</h1>"
                '<iframe src="https://giphy.com/embed/S6VGjvmFRu5Qk" width="385" height="480" frameBorder="0" '
                'class="giphy-embed" allowFullScreen></iframe><p>'
                '<a href="https://giphy.com/gifs/ufo-abduction-S6VGjvmFRu5Qk">via GIPHY</a></p>')
    else:
        return ("<h1 style='color: green'>You found me!</h1>"
                '<iframe src="https://giphy.com/embed/VOPK1BqsMEJRS" width="400" height="480" frameBorder="0" '
                'class="giphy-embed" allowFullScreen></iframe><p>'
                '<a href="https://giphy.com/gifs/cat-hello-hey-VOPK1BqsMEJRS">via GIPHY</a></p>')


if __name__ == "__main__":
    app.run(debug=True)
