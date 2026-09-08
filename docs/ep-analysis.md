# Equivalence Partitioning Analysis

## 1. Number of Books on Loan

Business Rule: A member may have between 0 and 5 books on loan simultaneously.

| Equivalence Class | Input Range | Valid/Invalid | Representative Value |
|---|---|---|---|
| Valid | 0–5 books | Valid | 3 |
| Invalid | 6+ books | Invalid | 6 |

## 2. ISBN Field

Business Rule: ISBN must contain exactly 13 numeric digits.

| Equivalence Class | Input | Valid/Invalid | Representative Value |
|---|---|---|---|
| Valid 13-digit ISBN | Exactly 13 numeric digits | Valid | `9780132350884` |
| Empty string | Empty string | Invalid | `""` |
| Too-short string | Less than 13 digits | Invalid | `123456789` |
| Letters/Symbols | Contains letters or symbols | Invalid | `9780132350ABC` |

## 3. Final Test Result

After implementing all Equivalence Partitioning tests, the complete test suite was executed.

```text
21 passed
