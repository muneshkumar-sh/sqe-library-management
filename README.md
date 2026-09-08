# SQE Library Management System

A Library Management System developed as part of the **Software Quality Engineering (SQE)** course. The project demonstrates the practical application of software quality practices using GitHub, automated testing, documentation, and structured development workflows.

---

## 📌 Project Description

The **SQE Library Management System** provides basic functionality for managing library resources. The project is also used to demonstrate software testing and quality engineering techniques throughout the development process.

The system focuses on:

- Managing books
- Managing library members
- Searching for books
- Testing system functionality
- Applying Software Quality Engineering practices

---

## 🎯 Project Objectives

The main objectives of this project are to:

- Manage library books
- Manage library members
- Search for books
- Design and execute test cases
- Apply Equivalence Partitioning and other testing techniques
- Track development tasks using GitHub Issues
- Maintain source code, tests, and documentation in an organized repository
- Practice a structured Git and GitHub workflow

---

## ✨ Main Features

### 📚 Book Management
- Store and manage book information
- Validate book-related data
- Apply business rules to book operations

### 👤 Member Management
- Manage library member information
- Apply borrowing rules and limits

### 🔍 Book Search
- Support searching for books within the library system

### 🧪 Software Testing
- Automated tests using `pytest`
- Equivalence Partitioning test cases
- Validation of valid and invalid inputs
- Test execution and result tracking

---

## 🧰 Technologies Used

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
│   └── workflows/          # GitHub Actions workflows
│
├── docs/                   # Project documentation
│   └── ep-analysis.md      # Equivalence Partitioning analysis
│
├── screenshots/            # Lab and project screenshots
│
├── src/                    # Source code
│   ├── __init__.py
│   ├── book.py
│   └── library.py
│
├── tests/                  # Automated test cases
│   ├── test_book.py
│   ├── test_fine_tier.py
│   ├── test_borrow_limit.py
│   └── test_validate_isbn.py
│
├── .gitignore
├── LICENSE
└── README.md
