class Student:
    def __init__(self, name):
        self.student_name = name
        self.scores = []

    def add_score(self, score):
        if not isinstance(score, (int, float)):
            raise ValueError("Score must be numeric")
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.scores.append(score)

    def get_average(self):
        """Calculate and return the student's average score."""
        return sum(self.scores) / len(self.scores) if self.scores else 0