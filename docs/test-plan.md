# LibraryHub Software Test Plan

## 1. Introduction

This test plan defines the testing activities for the LibraryHub module. The purpose is to verify that book management, book issuing, returning, searching, and validation functions behave according to their requirements. Testing will focus on functional behavior and error handling of the current LibraryHub codebase. The test plan follows an IEEE 829-style structure.

## 2. Test Items

The main test item is the LibraryHub Python module located in `src/library.py`. The module contains the `Book` and `Library` classes. The functions under test include book creation, adding books, issuing books, returning books, and searching books by title.

## 3. Features to be Tested

The following features will be tested:

- Creating books with valid and invalid quantities
- Adding new books
- Rejecting duplicate book IDs
- Issuing available books
- Rejecting issue requests when no copies are available
- Returning books
- Searching books by title
- Error handling for invalid library operations

## 4. Features Not to be Tested

Graphical user interface testing is out of scope because the current LibraryHub implementation is a Python module and does not provide a graphical user interface. Database, network, and performance testing are also excluded because the current implementation does not use an external database or network service. ISBN validation, member management, borrowing limits, and fine calculation will be recorded as blocked where applicable because these features are not implemented in the current codebase.

## 5. Test Approach

Testing will primarily use manual execution through the Python interpreter. Both positive and negative test cases will be used to verify normal behavior and error handling. Test cases will contain unique IDs, requirements, preconditions, steps, expected results, priorities, and test types. Regression testing will focus on previously identified LibraryHub defects from Lab 3.

## 6. Pass/Fail Criteria

The test execution will be considered successful when at least 95% of executable planned test cases pass and no Critical severity defect remains open. A test will be marked Failed when the actual behavior differs from its expected result. A test will be marked Blocked when the required functionality is not available in the current implementation.

## 7. Test Deliverables

The testing deliverables will include this Test Plan, a set of 12 documented test cases, a Requirements Traceability Matrix, and recorded execution results. GitHub Issues will be created for defects discovered during execution. Test evidence and relevant issue references will be retained in the repository.

## 8. Environmental Needs

Testing will be performed on the local development environment using Git Bash and Python. The LibraryHub source code will be taken from the `main` branch of the repository. No external database or network service is required for the current module.

## 9. Schedule

The planned testing activity follows the three-hour laboratory schedule. Approximately 60 minutes will be used for test planning, 75 minutes for test case preparation, 30 minutes for requirements traceability, and 35 minutes for manual execution. Any additional time will be used for documenting failures and GitHub Issues.

## 10. Risks

The main risk is that some scenarios required by the laboratory are not implemented in the current LibraryHub codebase. Such cases may be blocked rather than producing meaningful execution results. Another risk is that existing defects identified in Lab 3 may cause test failures. Test results will be documented honestly and failures will be linked to GitHub Issues where required.
