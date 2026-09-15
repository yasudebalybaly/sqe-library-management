import pytest
from src.gradebook import Student, Roster
@pytest.mark.parametrize("score_count,expected_valid", [
    (0, False),
    (1, True),
    (2, True),
    (5, True),
    (6, True),
    (7, False),
])
def test_roster_score_count_boundaries(score_count, expected_valid):
    student = Student("Test Student")

    for i in range(score_count):
        student.add_score(50)

    roster = Roster()

    if expected_valid:
        roster.add_student(student)
        assert student in roster.students
    else:
        with pytest.raises(ValueError):
            roster.add_student(student)
