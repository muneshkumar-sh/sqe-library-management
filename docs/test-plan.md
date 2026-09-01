# LibraryHub Software Test Plan

## 1. Introduction

### 1.1 Purpose

This Test Plan defines the testing approach for the LibraryHub module of the
Library Management System. The purpose is to verify that the core library
operations work correctly and handle both valid and invalid inputs. The plan
provides a structured basis for designing, executing, and evaluating test cases.

### 1.2 Objectives

The main objectives are:

- Verify the correctness of core LibraryHub functions.
- Identify defects in book and member operations.
- Verify borrowing and returning rules.
- Verify fine calculation.
- Ensure invalid operations are handled correctly.
- Maintain traceability between requirements and test cases.

---

## 2. Test Items

The following LibraryHub functionality will be tested:

- Adding books to the library.
- ISBN validation and duplicate ISBN prevention.
- Borrowing books.
- Returning books.
- Availability of book copies.
- Member borrowing limits.
- Fine calculation for overdue books.
- Error handling for invalid library operations.

---

## 3. Features to be Tested

The following features are included in testing:

1. Adding a new book with a valid ISBN.
2. Rejecting duplicate ISBNs.
3. Rejecting malformed ISBNs.
4. Borrowing a book when copies are available.
5. Preventing borrowing when no copies are available.
6. Returning a book currently on loan.
7. Handling invalid book returns.
8. Enforcing the member borrowing limit.
9. Calculating fines correctly.
10. Handling fine calculation at boundary conditions.

---

## 4. Features Not to be Tested

The graphical user interface (UI) is not included in this test plan because the
current LibraryHub testing focuses on the core library logic and functions.
Database performance and large-scale load testing are also outside the scope
of this lab. These areas can be tested separately in future testing activities.

---

## 5. Test Approach

Testing will mainly use functional and negative testing techniques.

### Functional Testing

Valid inputs will be provided to verify that the LibraryHub functions perform
their intended operations correctly.

### Negative Testing

Invalid inputs and invalid operations will be tested to verify that the system
rejects them correctly and produces the expected errors.

### Boundary Testing

Boundary conditions such as the maximum allowed number of borrowed books and
fine calculation limits will be tested.

### Regression Testing

Previously working functionality will be checked again after any defect is
fixed to ensure that the change has not introduced new problems.

---

## 6. Pass/Fail Criteria

A test case will be marked **PASS** when the actual result matches the expected
result. A test case will be marked **FAIL** when the actual result differs from
the expected result.

The overall testing will be considered successful when:

- At least **95% of the planned test cases pass**.
- **0 Critical defects** remain open.
- All **6–8 defined requirements** have at least one linked test case.
- All failed test cases have a corresponding GitHub Issue.
- No unresolved High-priority defect prevents the core LibraryHub operations
  from working.

---

## 7. Test Deliverables

The following deliverables will be produced:

- `docs/test-plan.md` — Software Test Plan.
- `docs/test-cases.md` — Detailed test cases.
- `docs/rtm.md` — Requirements Traceability Matrix.
- Manual test execution results.
- GitHub Issues for defects discovered during testing.
- Screenshots or other evidence where required.

---

## 8. Test Environment

Testing will be performed using the existing LibraryHub project repository on
GitHub.

The test environment will include:

- Operating System: Ubuntu/Linux or the existing development environment.
- Programming Language: Python.
- Source Code: Current LibraryHub implementation.
- Test Execution: Python shell/manual execution.
- Version Control: Git and GitHub.
- Documentation Format: Markdown.

Testing will be performed against the current version of the LibraryHub code
available in the repository.

---

## 9. Test Schedule

The testing activities will follow the Lab 4 schedule:

| Activity | Planned Time |
|---|---:|
| Test Plan preparation | 60 minutes |
| Test Case preparation | 75 minutes |
| Requirements Traceability Matrix | 30 minutes |
| Manual Test Execution | 35 minutes |
| **Total** | **3 hours** |

---

## 10. Risks and Mitigation

| Risk | Impact | Mitigation |
|---|---|---|
| Incorrect test data | Medium | Prepare valid and invalid test data before execution |
| Existing defects in the code | High | Record failures and create GitHub Issues |
| Untested requirements | High | Use the RTM to verify requirement coverage |
| Incorrect expected results | Medium | Review requirements before test execution |
| Test environment problems | Medium | Verify the project runs before testing |

---

## 11. Roles and Responsibilities

The student/tester is responsible for:

- Preparing the Test Plan.
- Designing the test cases.
- Mapping requirements to test cases.
- Executing the test cases.
- Recording Pass/Fail/Blocked results.
- Reporting defects through GitHub Issues.
- Maintaining testing documentation.

---

## 12. Entry Criteria

Testing can begin when:

- The LibraryHub source code is available.
- The project can be executed successfully.
- The required requirements have been identified.
- Test data is available.
- The testing environment is ready.

---

## 13. Exit Criteria

Testing will be completed when:

- All 12 planned test cases have been executed.
- Each test case has a recorded result.
- Requirements have been mapped in the RTM.
- Defects found during testing have been reported.
- At least 95% of test cases pass.
- No Critical defects remain open.

---

## 14. Approval

This Test Plan is prepared for the Software Quality Engineering Lab 4
assessment and will be used as the basis for test case development and manual
test execution.
