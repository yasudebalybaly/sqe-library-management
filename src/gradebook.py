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


def letter_grade(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")

    if score <= 59:
        return "F"
    elif score <= 69:
        return "D"
    elif score <= 79:
        return "C"
    elif score <= 89:
        return "B"
    else:
        return "A"


class Roster:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(student.scores) < 1 or len(student.scores) > 6:
            raise ValueError("Student must have between 1 and 6 scores")
        self.students.append(student)


def validate_name(name):
    if not isinstance(name, str):
        raise ValueError("Name must be a string")

    if len(name) == 0:
        raise ValueError("Name cannot be empty")

    if len(name) > 50:
        raise ValueError("Name cannot exceed 50 characters")

    for character in name:
        if not (character.isalpha() or character == " " or character == "-"):
            raise ValueError("Name can only contain letters, spaces and hyphens")

    return True