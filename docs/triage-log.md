# SQE Lab 03 — Defect Triage Log

## Triage Summary

| Rank | Defect | Severity | Priority | Decision |
|------|--------|----------|----------|----------|
| 1 | Empty ISBN accepted | High | High | Fix |
| 2 | Non-numeric rating not handled safely | High | High | Fix |
| 3 | Empty book title accepted | High | High | Fix |
| 4 | ISBN whitespace not normalized | Medium | Medium | Defer |
| 5 | Author whitespace not normalized | Low | Low | Defer |

## Triage Decisions

### 1. Empty ISBN Accepted
**Decision: Fix**

ISBN is a core identifier for a book. Accepting an empty ISBN can create invalid book records, so this issue has high priority.

### 2. Non-numeric Rating
**Decision: Fix**

Invalid rating input can cause an unexpected error. Since rating is an existing feature, this should be handled safely before release.

### 3. Empty Book Title
**Decision: Fix**

A book should have a valid title. Accepting an empty title can create incomplete book records and affect normal book management.

### 4. ISBN Whitespace
**Decision: Defer**

This issue affects data consistency but does not block the main functionality. It can be addressed in a future iteration.

### 5. Author Whitespace
**Decision: Defer**

This is mainly a formatting issue with low impact. It does not prevent normal book operations and can be postponed.

## Severity vs Priority

Severity describes the impact of a defect, while priority describes how urgently it should be fixed.

The first three defects are selected because they affect core Book functionality and have high priority.

The ISBN and author whitespace issues are deferred because they have lower impact and do not block the current release.

## Sprint Decision

### Fix This Sprint

- Empty ISBN accepted
- Non-numeric rating not handled safely
- Empty book title accepted

### Defer

- ISBN whitespace not normalized
- Author whitespace not normalized