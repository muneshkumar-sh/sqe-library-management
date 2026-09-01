# LibraryHub Test Plan

## 1. Introduction

This test plan defines how the LibraryHub system will be tested. It focuses on verifying core library operations and handling invalid inputs.

## 2. Test Items

The following functions will be tested:

* `add_book()`
* `borrow_book()`
* `return_book()`
* Fine calculation
* Member borrowing limit

## 3. Features to be Tested

* Adding books
* ISBN validation
* Borrowing and returning books
* Book availability
* Borrowing limits
* Fine calculation
* Error handling

## 4. Features Not to be Tested

The user interface is out of scope because this lab focuses on the LibraryHub core logic. Performance and load testing are also excluded.

## 5. Test Approach

Functional testing will verify normal operations. Negative testing will check invalid inputs and operations. Boundary testing will check limits such as maximum borrowing and fine boundaries. Regression testing will be performed after fixes.

## 6. Pass/Fail Criteria

* At least **95% of test cases must pass**.
* **0 Critical defects** should remain open.
* All requirements must have at least one linked test case.

## 7. Test Deliverables

* `docs/test-plan.md`
* `docs/test-cases.md`
* `docs/rtm.md`
* Test execution results
* GitHub Issues for discovered defects

## 8. Test Environment

* OS: Ubuntu/Linux
* Language: Python
* Repository: GitHub
* Testing: Manual/Python shell
* Documentation: Markdown

## 9. Schedule

| Activity       |   Time |
| -------------- | -----: |
| Test Plan      | 60 min |
| Test Cases     | 75 min |
| RTM            | 30 min |
| Manual Testing | 35 min |

## 10. Risks

* Incorrect test data
* Existing defects
* Untested requirements
* Incorrect expected results

## 11. Roles

The tester will create test cases, execute tests, record results, update the RTM, and report defects.

## 12. Entry Criteria

* LibraryHub code is available.
* Requirements are identified.
* Test environment is ready.

## 13. Exit Criteria

* All 12 test cases are executed.
* Results are recorded.
* Requirements are traced.
* Defects are reported.
* At least 95% tests pass.
* No Critical defects remain open.
