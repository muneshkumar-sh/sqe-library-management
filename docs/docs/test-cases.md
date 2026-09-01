# LibraryHub Test Cases

| ID | Title | Requirement | Preconditions | Steps | Expected | Priority | Type |
|---|---|---|---|---|---|---|---|
| TC-01 | Valid ISBN | REQ-01 | System is running | Create Book with valid ISBN | Book is created successfully | High | Positive |
| TC-02 | Empty ISBN | REQ-01 | System is running | Create Book with empty ISBN | `ValueError` is raised | High | Negative |
| TC-03 | Whitespace ISBN | REQ-01 | System is running | Create Book with whitespace ISBN | `ValueError` is raised | High | Negative |
| TC-04 | None ISBN | REQ-01 | System is running | Create Book with `None` ISBN | `ValueError` is raised | High | Negative |
| TC-05 | Valid title | REQ-02 | Valid ISBN provided | Create Book with valid title | Book is created with correct title | High | Positive |
| TC-06 | Empty title | REQ-02 | Valid ISBN provided | Create Book with empty title | `ValueError` is raised | High | Negative |
| TC-07 | Whitespace title | REQ-02 | Valid ISBN provided | Create Book with whitespace title | `ValueError` is raised | High | Negative |
| TC-08 | Non-numeric rating | REQ-03 | Valid Book exists | Add `"five"` as rating | `ValueError` is raised | High | Negative |
| TC-09 | Valid integer rating | REQ-03 | Valid Book exists | Add rating `4` | Rating is set to 4 | High | Positive |
| TC-10 | Valid decimal rating | REQ-03 | Valid Book exists | Add rating `4.5` | Rating is set to 4.5 | Medium | Positive |
| TC-11 | Rating above maximum | REQ-03 | Valid Book exists | Add rating `6` | `ValueError` is raised | High | Negative |
| TC-12 | Rating below minimum | REQ-03 | Valid Book exists | Add rating `-1` | `ValueError` is raised | High | Negative |
