# Equivalence Partitioning Analysis

## 1. Number of Books on Loan

**Business Rule:** A member may have between 0 and 5 books on loan simultaneously.

| Equivalence Class | Input Range | Valid/Invalid | Representative Value |
|---|---|---|---|
| Valid | 0–5 books | Valid | 3 |
| Invalid | 6+ books | Invalid | 6 |

**Explanation:**  
The valid class contains all values from 0 to 5 books. A value of 3 is selected as a representative value. The invalid class contains 6 or more books because a member cannot borrow more than 5 books at the same time.

---

## 2. ISBN Field

**Business Rule:** ISBN must contain exactly 13 numeric digits.

| Equivalence Class | Input | Valid/Invalid | Representative Value |
|---|---|---|---|
| Valid 13-digit ISBN | Exactly 13 numeric digits | Valid | `9780132350884` |
| Empty string | Empty string | Invalid | `""` |
| Too-short string | Less than 13 digits | Invalid | `123456789` |
| Letters/Symbols | Contains letters or symbols | Invalid | `9780132350ABC` |

**Explanation:**  
The valid class contains ISBN values with exactly 13 numeric digits. Empty, shorter, or non-numeric ISBN values belong to invalid classes and should be rejected by the system.

---

## 3. Days Overdue

**Business Rule:** The number of overdue days determines the fine tier.

| Equivalence Class | Input Range | Expected Result | Representative Value |
|---|---|---|---|
| Invalid | Less than 0 | ValueError | -3 |
| None | 0 | None | 0 |
| Low | 1–7 | Low | 4 |
| Medium | 8–14 | Medium | 10 |
| High | 15–30 | High | 20 |
| Severe | 31+ | Severe | 45 |

**Explanation:**  
Each range represents one equivalence class. One representative value from each class is used for testing. Negative values are invalid and should raise a `ValueError`.

---

## 4. Final Test Result

After implementing the Equivalence Partitioning tests, the complete test suite was executed.

```text
21 passed
