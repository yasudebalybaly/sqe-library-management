import pytest
from src.gradebook import Student, Roster


@pytest.mark.parametrize("number_of_scores,expected_error", [
    (0, True),
    (3, False),
    (8, True),
])
def test_roster_score_classes(number_of_scores, expected_error):
    student = Student("Muhammad Yasir")

    for score in range(number_of_scores):
        student.add_score(50)

    roster = Roster()

    if expected_error:
        with pytest.raises(ValueError):
            roster.add_student(student)
    else:
        roster.add_student(student)
        assert student in roster.students