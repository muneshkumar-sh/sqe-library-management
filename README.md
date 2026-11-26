# SQE Library Management System

## Project Description

The SQE Library Management System is a project developed as part of the Software Quality Engineering (SQE) course.

The project focuses on developing a simple Library Management System while applying different Software Quality Engineering practices throughout the semester, from basic development and unit testing to API testing, TDD, and Selenium UI testing.

## Project Objectives

- Manage library books.
- Manage library members.
- Search and view books.
- Borrow and return books.
- Check member fines.
- Practice different software testing techniques.
- Use GitHub for version control and collaboration.
- Maintain code quality using SonarCloud.

## Main Features

- **Book Management:** Add books and view the book catalog.
- **Book Search:** Search for a book using its ISBN.
- **Member Management:** Work with registered library members.
- **Borrow Books:** Allow members to borrow available books.
- **Return Books:** Allow members to return borrowed books.
- **Fine Details:** Check fines for library members.
- **Book Ranking:** Rank books based on borrowing popularity.
- **Library Web Interface:** A simple web interface for interacting with the system.

## Technologies Used

- Python
- Flask
- HTML, CSS, JavaScript
- Pytest
- Selenium
- Git and GitHub
- GitHub Actions
- SonarCloud

## Testing and Quality Practices

During the labs, different software quality and testing techniques were implemented:

- Unit Testing
- API Testing
- Boundary Value Analysis (BVA)
- Equivalence Partitioning
- Parameterized Testing
- Test-Driven Development (TDD)
- Code Coverage Analysis
- Selenium UI Testing
- Page Object Model (POM)
- Explicit Waits
- Fixed Sleep vs Explicit Wait Comparison
- CI/CD using GitHub Actions
- Code Quality Analysis using SonarCloud

## Project Structure

```text
sqe-library-management/
│
├── src/
│   ├── api/
│   │   └── app.py
│   ├── webapp/
│   │   └── templates/
│   │       └── index.html
│   ├── book.py
│   └── library.py
│
├── tests/
│   ├── test_api.py
│   ├── test_book.py
│   ├── test_borrow_limit.py
│   ├── test_borrow_parametrized.py
│   ├── test_borrow_percentile.py
│   ├── test_catalog_page.py
│   ├── test_explicit_waits.py
│   ├── test_fine_tier.py
│   ├── test_fine_tier_bva.py
│   ├── test_library_catalog.py
│   ├── test_library_export.py
│   ├── test_rank_books.py
│   └── test_validate_isbn.py
│
├── pages/
│   └── catalog_page.py
│
├── experiments/
│   └── fixed_sleep.py
│
├── docs/
│   ├── test-plan.md
│   ├── tdd-log.md
│   ├── selenium-notes.md
│   └── other lab documentation
│
├── screenshots/
│
├── .github/
│   └── workflows/
│       └── build.yml
│
├── requirements.txt
├── pytest.ini
├── sonar-project.properties
└── README.md
```

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/muneshkumar-sh/sqe-library-management.git
```

### 2. Open the Project Folder

```bash
cd sqe-library-management
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m src.api.app
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000/
```

### 5. Run Tests

Run all tests with coverage:

```bash
python -m pytest tests/ --cov=src --cov-report=xml
```

## Code Quality and CI/CD

GitHub Actions is used to automatically run the build and SonarCloud analysis when changes are pushed or pull requests are created.

SonarCloud is used to check code quality, identify issues, and monitor code coverage.

## Project Progress

The project was developed and improved through the SQE lab activities up to Lab 13. Each lab introduced different software quality practices, testing techniques, and improvements to the Library Management System.

## Author

**Munesh Kumar**

Software Engineering Student