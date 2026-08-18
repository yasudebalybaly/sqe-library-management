# Git Workflow Notes

## Task 3 - Merge Conflict

### Cause of the Conflict

A merge conflict was deliberately created between feature/rename-field-a and feature/rename-field-b.

Both branches modified the same original line in src/gradebook.py, but changed it to different values.

Branch A changed:
self.name = name

to:
self.student_name = name

Branch B changed the same original line to:
self.full_name = name

Because both branches changed the same line differently, Git could not automatically determine which version should be kept.

### Conflict Resolution

The conflict was resolved locally by merging main into feature/rename-field-b using:

git merge main

Git reported a content conflict in:
src/gradebook.py

The conflict markers were removed manually, and the final version selected was:

self.full_name = name

The resolved file was staged and committed using:

git add src/gradebook.py

git commit -m "fix(gradebook): resolve student field rename conflict"

The resolved branch was then pushed to GitHub.

### Result

The merge conflict was successfully resolved and the Pull Request was updated with the resolved changes.

---

## Task 4 - Commit Hygiene Audit

### Last 10 Commits

f633783 fix(gradebook): resolve student field rename conflict
9da7016 refactor(gradebook): use full name field
b988631 Merge pull request #6 from yasudebalybaly/feature/rename-field-a
d33b532 refactor(gradebook): rename student field
e3f9b71 Merge pull request #5 from yasudebalybaly/feature/add-student
d2d1f48 fix(gradebook): validate score input type
c83f63e fix(gradebook): reject negative scores
fa33abb feat(gradebook): add score method
4e3e760 feat(gradebook): add Student class
5f7d152 chore: add project structure

### Two Weak Commit Messages

#### Weak Commit Message 1

Merge pull request #6 from yasudebalybaly/feature/rename-field-a

Better message:
refactor(gradebook): rename student field

Reason:
The improved message clearly describes the actual code change instead of only describing the Pull Request operation.

#### Weak Commit Message 2

Merge pull request #5 from yasudebalybaly/feature/add-student

Better message:
feat(gradebook): add student score functionality

Reason:
The improved message clearly describes the feature introduced by the change.

### Why Better Commit Messages Matter

Good commit messages make project history easier to understand, review, search, and maintain. Conventional Commit prefixes such as feat, fix, refactor, and chore clearly communicate the type of change.

---

## Task 5 - Interactive Rebase Practice

This section will be completed after performing the interactive rebase exercise.