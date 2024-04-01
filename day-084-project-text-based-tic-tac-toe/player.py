from random import randint


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.score = 0
        self.mark = mark
        self.is_ai = False

    def place_mark(self):
        return self.mark

    def toggle_ai(self):
        self.name = "Computer"
        self.is_ai = True

    def place_mark_as_ai(self):
        return f"{randint(1, 3)},{randint(1, 3)}"
