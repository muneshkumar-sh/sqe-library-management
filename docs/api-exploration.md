
New-Item -ItemType Directory -Force -Path docs | Out-Null

@'
# API Manual Exploration - SQE Lab 12

## Objective
Manually explore all five Library Management API endpoints using curl.exe before implementing automated tests.

Base URL: `http://127.0.0.1:5000`

## Test 1 - Retrieve Unknown Book

- **Method:** GET
- **Path:** `/books/9999999999`
- **Body:** None
- **Status:** 404 NOT FOUND

Response:
```json
{
  "error": "Book not found"
}
```

## Test 2 - Create a Book

- **Method:** POST
- **Path:** `/books`
- **Body:**
```json
{
  "title": "Clean Code",
  "isbn": "9780132350884",
  "author": "Robert C. Martin",
  "total_copies": 3
}
```
- **Status:** 201 CREATED

Response:
```json
{
  "author": "Robert C. Martin",
  "available_copies": 3,
  "isbn": "9780132350884",
  "title": "Clean Code"
}
```

## Test 3 - Retrieve Existing Book

- **Method:** GET
- **Path:** `/books/9780132350884`
- **Body:** None
- **Status:** 200 OK

Response:
```json
{
  "author": "Robert C. Martin",
  "available_copies": 3,
  "isbn": "9780132350884",
  "title": "Clean Code"
}
```

## Test 4 - Borrow a Book

- **Method:** POST
- **Path:** `/members/501/borrow`
- **Body:**
```json
{
  "isbn": "9780132350884"
}
```
- **Status:** 200 OK

Response:
```json
{
  "available_copies": 2,
  "isbn": "9780132350884",
  "member_id": 501
}
```

## Test 5 - Return a Book

- **Method:** POST
- **Path:** `/members/501/return`
- **Body:**
```json
{
  "isbn": "9780132350884"
}
```
- **Status:** 200 OK

Response:
```json
{
  "available_copies": 3,
  "isbn": "9780132350884",
  "member_id": 501,
  "message": "Book returned successfully"
}
```

## Test 6 - Invalid Request (Missing ISBN)

- **Method:** POST
- **Path:** `/books`
- **Body:**
```json
{
  "title": "Python Basics",
  "author": "John Smith"
}
```
- **Status:** 400 BAD REQUEST

Response:
```json
{
  "error": "Missing required field: isbn"
}
```

## Test 7 - Invalid Request (Wrong Data Type)

- **Method:** POST
- **Path:** `/books`
- **Body:**
```json
{
  "title": "Python Basics",
  "isbn": "9780132350884",
  "author": "John Smith",
  "total_copies": "five"
}
```
- **Status:** 400 BAD REQUEST

Response:
```json
{
  "error": "total_copies must be an integer"
}
```

## Test 8 - Retrieve Member Fines

- **Method:** GET
- **Path:** `/members/501/fines`
- **Body:** None
- **Status:** 200 OK

Response:
```json
{
  "fine": 0,
  "member_id": 501
}
```

## Test 9 - Retrieve Fines for Unknown Member

- **Method:** GET
- **Path:** `/members/999/fines`
- **Body:** None
- **Status:** 404 NOT FOUND

Response:
```json
{
  "error": "Member not found"
}
```

## Exploration Summary

| Test | Endpoint | Status | Result |
|---|---|---|---|
| 1 | GET /books/9999999999 | 404 | PASS |
| 2 | POST /books | 201 | PASS |
| 3 | GET /books/9780132350884 | 200 | PASS |
| 4 | POST /members/501/borrow | 200 | PASS |
| 5 | POST /members/501/return | 200 | PASS |
| 6 | POST /books (missing ISBN) | 400 | PASS |
| 7 | POST /books (wrong type) | 400 | PASS |
| 8 | GET /members/501/fines | 200 | PASS |
| 9 | GET /members/999/fines | 404 | PASS |

**Total manual exploration tests: 9**

**All five API endpoints were manually exercised.**

Two deliberately invalid requests were tested successfully.

The observed HTTP status codes matched the expected behavior.

## Conclusion

Manual API exploration was completed using curl.exe before automated testing. Successful operations, unknown resources, missing fields, and incorrect data types were examined. The observed request and response pairs are documented above as informal test design notes.
'@ | Set-Content -Path docs/api-exploration.md -Encoding UTF8

