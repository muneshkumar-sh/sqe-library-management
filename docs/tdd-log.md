# Lab 08 — Test-Driven Development Log

## Feature: Rank Books by Popularity

**Branch:** `feature/rank-books-tdd`

**Objective:** Rank library books by their total recorded borrowings in descending order. When books have equal borrowing counts, sort them alphabetically by title.

## TDD Cycles

### Cycle 1 — Empty Catalog

- **RED:** Added a test verifying that an empty library returns an empty list.
- **GREEN:** Implemented the minimum function returning an empty list.
- **Result:** Test passed.

### Cycle 2 — Single Book

- **RED:** Added a test verifying that a library containing one book returns that book.
- **GREEN:** Updated the implementation to return the books in the library.
- **Result:** Test passed.

### Cycle 3 — Popularity Ranking

- **RED:** Added a test with three books having different borrowing counts.
- **GREEN:** Counted recorded borrowings using ISBNs and sorted books by borrowing count in descending order.
- **Result:** Test passed.

### Cycle 4 — Alphabetical Tie-Breaking

- **RED:** Added a test verifying alphabetical ordering for books with equal borrowing counts.
- **GREEN:** Updated the sorting key to use borrowing count followed by lowercase title.
- **Result:** Test passed.

### Cycle 5 — Never-Borrowed Book

- Added an edge-case test verifying that a book with no recorded borrowings ranks after a borrowed book.
- **Result:** Test passed.

## Refactoring

Refactored the ranking tests to reuse a `populated_library` pytest fixture, reducing repeated setup code.

## Verification

- Ranking tests: **5 passed**
- Full regression suite: **57 passed**
- Refactoring commit: `d530e48`

## Retrospective

This lab helped me practise the Red-Green-Refactor cycle. I learned to write a failing test before implementing a feature, then add only enough code to make it pass. The tests verified popularity ranking, alphabetical tie-breaking, and handling of books that have never been borrowed. Refactoring with a pytest fixture reduced repeated setup while preserving test behavior. Finally, running the full regression suite helped confirm that the new feature did not break existing functionality.