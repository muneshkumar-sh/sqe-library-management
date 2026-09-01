# LibraryHub Test Cases

| ID    | Title                   | Requirement | Preconditions                                 | Steps                            | Expected                                          | Priority | Type                  |
| ----- | ----------------------- | ----------- | --------------------------------------------- | -------------------------------- | ------------------------------------------------- | -------- | --------------------- |
| TC-01 | Add valid book          | REQ-01      | Library is running                            | Add a book with a new valid ISBN | Book is added successfully                        | High     | Positive / Functional |
| TC-02 | Reject duplicate ISBN   | REQ-01      | Book with ISBN already exists                 | Add another book with same ISBN  | `ValueError` is raised and duplicate is not added | High     | Negative / Functional |
| TC-03 | Reject malformed ISBN   | REQ-01      | Library is running                            | Add a book with an invalid ISBN  | Invalid ISBN is rejected                          | High     | Negative / Functional |
| TC-04 | Borrow available book   | REQ-02      | Book has available copies; member is eligible | Borrow the book                  | Loan is created and available copies decrease     | High     | Positive / Functional |
| TC-05 | Borrow unavailable book | REQ-02      | Book has zero available copies                | Try to borrow the book           | Borrow operation is rejected                      | High     | Negative / Functional |
| TC-06 | Return borrowed book    | REQ-03      | Member currently has the book on loan         | Return the book                  | Loan is closed and copy becomes available         | High     | Positive / Functional |
| TC-07 | Return book not on loan | REQ-03      | Member does not have the book on loan         | Try to return the book           | Return operation is rejected                      | Medium   | Negative / Functional |
| TC-08 | Borrow at allowed limit | REQ-04      | Member has 4 borrowed books                   | Borrow a fifth book              | Fifth book is successfully borrowed               | High     | Boundary / Functional |
| TC-09 | Exceed borrowing limit  | REQ-04      | Member already has 5 borrowed books           | Try to borrow another book       | Borrow operation is rejected                      | High     | Negative / Boundary   |
| TC-10 | Zero days overdue fine  | REQ-05      | Book is returned on due date                  | Return with 0 overdue days       | Fine is calculated as 0                           | Medium   | Boundary / Functional |
| TC-11 | Mid-range overdue fine  | REQ-05      | Book is overdue by 5 days                     | Return the book                  | Correct fine for 5 overdue days is calculated     | Medium   | Functional            |
| TC-12 | Fine at tier boundary   | REQ-05      | Book is overdue at a fine-tier boundary       | Return the book                  | Correct boundary fine is calculated               | High     | Boundary / Functional |

## Test Execution Results

| ID    | Result  | Note           |
| ----- | ------- | -------------- |
| TC-01 | Pending | To be executed |
| TC-02 | Pending | To be executed |
| TC-03 | Pending | To be executed |
| TC-04 | Pending | To be executed |
| TC-05 | Pending | To be executed |
| TC-06 | Pending | To be executed |
| TC-07 | Pending | To be executed |
| TC-08 | Pending | To be executed |
| TC-09 | Pending | To be executed |
| TC-10 | Pending | To be executed |
| TC-11 | Pending | To be executed |
| TC-12 | Pending | To be executed |
