# LibraryHub Requirements Traceability Matrix

## Purpose

This Requirements Traceability Matrix (RTM) maps LibraryHub functional requirements to the test cases that verify them. Each requirement has at least one associated test case to ensure complete test coverage.

| Requirement ID | Requirement Description | Test Case IDs | Coverage |
|---|---|---|---|
| REQ-01 | The system shall allow a new book to be added with valid book information. | TC-001 | Covered |
| REQ-02 | The system shall reject a book when its ISBN already exists in the catalog. | TC-002 | Covered |
| REQ-03 | The system shall reject a book when its ISBN format is malformed. | TC-003 | Covered |
| REQ-04 | The system shall allow a member to borrow a book when copies are available. | TC-004 | Covered |
| REQ-05 | The system shall reject borrowing when no copies of the requested book are available. | TC-005 | Covered |
| REQ-06 | The system shall correctly process book returns and reject returns for books not currently on loan by the member. | TC-006, TC-007 | Covered |
| REQ-07 | The system shall enforce the maximum number of books a member is allowed to borrow. | TC-008, TC-009 | Covered |
| REQ-08 | The system shall calculate fines according to the number of overdue days and applicable fine tier. | TC-010, TC-011, TC-012 | Covered |

## Traceability Summary

- Total functional requirements: 8
- Total test cases: 12
- Requirements with at least one test case: 8
- Requirements without test coverage: 0
- Overall requirement coverage: 100%

## Coverage Notes

All eight defined functional requirements are mapped to at least one test case. Positive, negative, and boundary scenarios are included where applicable. Some test cases may be marked BLOCKED during execution because the current LibraryHub implementation does not yet provide ISBN validation, member management, borrowing limits, or fine calculation.
