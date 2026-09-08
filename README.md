# SQE Library Management System

> A Software Quality Engineering course project demonstrating software development, testing, documentation, and GitHub-based quality practices.

---

## 📖 Project Overview

The **SQE Library Management System** is a Python-based project developed for the **Software Quality Engineering (SQE)** course.

The project demonstrates how software quality practices can be applied throughout the development process. It includes source code, automated tests, documentation, screenshots, and GitHub workflow management.

The system focuses on basic library operations such as book management, borrowing limits, fine calculation, and ISBN validation.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Manage library books and related information
- Apply library business rules
- Implement book borrowing functionality
- Validate ISBN information
- Calculate fine tiers based on overdue days
- Design test cases using **Equivalence Partitioning**
- Perform automated testing using **Pytest**
- Track project activities using GitHub
- Maintain organized source code, tests, and documentation
- Practice Git-based version control and development workflows

---

## ✨ Key Features

### 📚 Book Management

- Create and manage book information
- Validate book details
- Validate ISBN values

### 📖 Library Management

- Borrow books for library members
- Enforce the maximum borrowing limit
- Track the number of books borrowed by a member

### 💰 Fine Management

- Calculate fine tiers according to overdue days
- Handle invalid negative overdue values

### 🧪 Automated Testing

- Test valid and invalid inputs
- Apply Equivalence Partitioning
- Use Pytest for automated test execution
- Verify system behavior through test cases

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Application development |
| **Pytest** | Automated testing |
| **Git** | Version control |
| **GitHub** | Repository and project management |
| **Markdown** | Documentation |

---

## 📁 Project Structure

```text
sqe-library-management/
│
├── .github/
│   └── workflows/
│
├── docs/
│   ├── .gitkeep
│   ├── ep-analysis.md
│   ├── test-plan.md
│   ├── triage-log.md
│   └── workflow-notes.md
│
├── screenshots/
│   ├── .gitkeep
│   ├── Task04-Last 10 commits.png
│   └── Task04-Last-10-commits.png
│
├── src/
│   ├── .gitkeep
│   ├── __init__.py
│   ├── book.py
│   └── library.py
│
├── tests/
│   ├── .gitkeep
│   ├── test_book.py
│   ├── test_borrow_limit.py
│   ├── test_fine_tier.py
│   └── test_validate_isbn.py
│
├── .gitignore
├── LICENSE
└── README.md
