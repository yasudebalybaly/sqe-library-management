class Student:
    # Constructor method used to create a new Student object
    def __init__(self, name):

        # Store the student's name
        self.student_name = name

        # Create an empty list to store the student's scores
        self.scores = []

    def add_score(self, score):
        # Add a new score to the student's score list

        # Check whether the score is a number
        # Only integers and decimal numbers are accepted
        if not isinstance(score, (int, float)):

            # Show an error if the score is not numeric
            raise ValueError("Score must be numeric")

        # Check whether the score is negative
        if score < 0:

            # Show an error because negative scores are not allowed
            raise ValueError("Score cannot be negative")

        # Add the valid score to the student's score list
        self.scores.append(score)

    def get_average(self):
        # Calculate and return the student's average score

        # If the student has scores, calculate the average
        # If there are no scores, return 0
        return sum(self.scores) / len(self.scores) if self.scores else 0


def letter_grade(score):
    # Convert a numerical score into a letter grade

    # Check that the score is between 0 and 100
    if score < 0 or score > 100:

        # Show an error if the score is outside the valid range
        raise ValueError("Score must be between 0 and 100")

    # Scores from 0 to 59 receive F
    if score <= 59:
        return "F"

    # Scores from 60 to 69 receive D
    elif score <= 69:
        return "D"

    # Scores from 70 to 79 receive C
    elif score <= 79:
        return "C"

    # Scores from 80 to 89 receive B
    elif score <= 89:
        return "B"

    # Scores from 90 to 100 receive A
    else:
        return "A"


class Roster:
    # Constructor method used to create a new Roster object
    def __init__(self):

        # Create an empty list to store students
        self.students = []

    def add_student(self, student):
        # Add a student to the roster

        # Check that the student has at least 1 score
        # and no more than 6 scores
        if len(student.scores) < 1 or len(student.scores) > 6:

            # Show an error if the number of scores is invalid
            raise ValueError("Student must have between 1 and 6 scores")

        # Add the student to the roster
        self.students.append(student)


def validate_name(name):
    # Validate the name before it is used

    # Check whether the name is a string
    if not isinstance(name, str):

        # Show an error if the name is not a string
        raise ValueError("Name must be a string")

    # Check whether the name is empty
    if len(name) == 0:

        # Show an error if no name was provided
        raise ValueError("Name cannot be empty")

    # Check whether the name is longer than 50 characters
    if len(name) > 50:

        # Show an error if the name is too long
        raise ValueError("Name cannot exceed 50 characters")

    # Check every character in the name
    for character in name:

        # Allow only letters, spaces and hyphens
        if not (character.isalpha() or character == " " or character == "-"):

            # Show an error if an invalid character is found
            raise ValueError(
                "Name can only contain letters, spaces and hyphens"
            )

    # Return True when all validation checks are passed
    return True
