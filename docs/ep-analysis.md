# Equivalence Partitioning Analysis

## 1. Score

The score input is divided into the following equivalence classes:

| Class | Input Range | Representative | Expected Result |
|---|---|---:|---|
| Invalid-low | Less than 0 | -10 | ValueError |
| F | 0-59 | 45 | F |
| D | 60-69 | 65 | D |
| C | 70-79 | 75 | C |
| B | 80-89 | 85 | B |
| A | 90-100 | 95 | A |
| Invalid-high | Greater than 100 | 150 | ValueError |

## 2. Number of Scores

A student must have between 1 and 6 scores.

| Class | Number of Scores | Representative | Expected Result |
|---|---|---:|---|
| Invalid-low | 0 | 0 | ValueError |
| Valid | 1-6 | 3 | Accepted |
| Invalid-high | 7 or more | 8 | ValueError |

## 3. Student Name

The student name must be a non-empty string with a maximum length of 50 characters. Only letters, spaces and hyphens are allowed.

| Class | Example | Expected Result |
|---|---|---|
| Valid typical name | Muhammad Yasir | Accepted |
| Valid name with spaces | Ali Khan | Accepted |
| Valid name with hyphen | Ahmed-Ali | Accepted |
| Empty name | "" | ValueError |
| Too long | 51 characters | ValueError |
| Contains digits | Yasir123 | ValueError |
| Contains symbols | Yasir@Khan | ValueError |

## EP Limitation

Equivalence Partitioning reduces the number of test cases by selecting representative values from each equivalence class. However, it can miss errors at the boundaries of classes.

For example, a defect at score 59, 60, 69, 70, 79, 80, 89, 90 or 100 may not be detected by representative values such as 45, 65, 75, 85 and 95.

Boundary Value Analysis is therefore useful for testing the edges of the equivalence classes.

## Test Results

The complete pytest test suite was executed after implementing the required functionality.

Final pytest result:

============================= 17 passed in 0.06s ==============================