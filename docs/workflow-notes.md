# Git Workflow Notes

## Task 3 — Deliberate Merge Conflict

### Cause of the Conflict

The merge conflict occurred because two branches modified the same lines
in `src/book.py` differently.

The `feature/rename-field-a` branch renamed `book_id` to `isbn`,
while the `feature/rename-field-b` branch renamed `book_id` to
`catalog_id`.

After the first branch was merged into `main`, Git could not automatically
combine the different changes from the second branch.

### Conflict Resolution

The conflict was first reproduced locally by merging `main` into
`feature/rename-field-b`.

Git marked `src/book.py` as conflicted using conflict markers:

- `<<<<<<< HEAD`
- `=======`
- `>>>>>>> main`

The conflict was resolved manually by keeping `isbn` as the book identifier
and removing the conflict markers.

The resolved file was then staged and committed, and the updated branch
was pushed to GitHub.

### Result

The merge conflict was successfully resolved locally and the GitHub pull
request was updated with the conflict resolution.
