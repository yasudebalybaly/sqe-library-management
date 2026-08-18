class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.scores.append(score)