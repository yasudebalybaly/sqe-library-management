# Library Management Defect Triage Log

## Sprint: v0.2 — Library Management

### Defect Priority Ranking

1. Book can be issued when no copy is available — High severity, P1 priority. This can create invalid availability records and directly affects library operations.
2. Duplicate book IDs overwrite existing books — High severity, P1 priority. This can cause existing book records to be lost or replaced.
3. Negative book quantities are accepted — Medium severity, P2 priority. This creates invalid inventory data and affects stock accuracy.
4. Returning a book can exceed the original inventory quantity — Medium severity, P2 priority. It creates inaccurate availability information, but the impact is limited to inventory tracking.
5. Book title search is case-sensitive — Low severity, P3 priority. The book can still be found using the exact capitalization, so the operational impact is limited.

## Severity and Priority Trade-offs

The unavailable-book defect is High severity and P1 because it can produce an invalid negative availability count and directly affect whether books can be issued. The duplicate book ID defect is also High severity and P1 because overwriting an existing record can result in loss of accurate library information.

The return-inventory defect has Medium severity and P2 priority because it produces inaccurate inventory data, but it does not immediately prevent other library operations. The case-sensitive search defect has Low severity and P3 priority because the book remains accessible when the correct capitalization is used.

## Sprint Decision

The first three defects will be fixed during this sprint. The return-inventory and case-sensitive search defects are deferred because their immediate business impact is lower and they can be addressed in a subsequent sprint.
