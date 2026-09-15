# Boundary Value Analysis - Letter Grade

## Function Under Test

The function under test is `letter_grade()`.

The valid score range is from 0 to 100.

The grading boundaries are:

* 0-59 = F
* 60-69 = D
* 70-79 = C
* 80-89 = B
* 90-100 = A

Boundary Value Analysis is used to test the values at the boundary, one value below the boundary, and one value above the boundary.

## Boundary Test Cases

| Boundary              | Value - 1 | Expected | Boundary Value | Expected | Value + 1 | Expected |
| --------------------- | --------: | -------- | -------------: | -------- | --------: | -------- |
| Lower domain boundary |        -1 | Invalid  |              0 | F        |         1 | F        |
| F/D boundary          |        59 | F        |             60 | D        |        61 | D        |
| D/C boundary          |        69 | D        |             70 | C        |        71 | C        |
| C/B boundary          |        79 | C        |             80 | B        |        81 | B        |
| B/A boundary          |        89 | B        |             90 | A        |        91 | A        |
| Upper domain boundary |        99 | A        |            100 | A        |       101 | Invalid  |

## Boundary Values Selected

The following values are selected for testing:

```text
-1, 0, 1
59, 60, 61
69, 70, 71
79, 80, 81
89, 90, 91
99, 100, 101
```

These values test both sides of every important boundary in the `letter_grade()` function.

## Purpose

The purpose of these tests is to find defects that may occur when a score is exactly at a grading boundary or just below or above it. This helps identify off-by-one errors that may not be detected by normal equivalence partitioning tests.

Boundary Value Analysis complements the Equivalence Partitioning testing performed in Lab 5.


## BVA Analysis - Roster

The Roster requires each student to have between 1 and 6 scores.

| Boundary | Value | Expected Result |
|---|---:|---|
| Minimum - 1 | 0 | Invalid |
| Minimum | 1 | Valid |
| Minimum + 1 | 2 | Valid |
| Maximum - 1 | 5 | Valid |
| Maximum | 6 | Valid |
| Maximum + 1 | 7 | Invalid |

These boundary values test the lower and upper limits of the allowed score count and help detect off-by-one errors.

## BVA Analysis - validate_name

The maximum allowed name length is 50 characters. An empty name is also invalid.

| Boundary | Value | Expected Result |
|---|---:|---|
| Minimum | 0 | Invalid |
| Minimum + 1 | 1 | Valid |
| Maximum - 1 | 49 | Valid |
| Maximum | 50 | Valid |
| Maximum + 1 | 51 | Invalid |

These values verify the lower and upper length boundaries and help detect incorrect handling of the 50-character limit.