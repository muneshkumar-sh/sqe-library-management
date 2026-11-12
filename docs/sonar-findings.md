# SonarCloud Findings Triage

Here is the triage of the top 8 issues found by SonarCloud in the `sqe-library-management` repository.

| Rule Name | File/Line | Severity | Explanation of Risk (in my own words) |
| :--- | :--- | :--- | :--- |
| `githubactions:S7637` | `.github/workflows/build.yml:L35` | **Critical** | Using tags like `@v3` for actions is dangerous. If a hacker takes over the action's repo and moves the tag, our pipeline will run their malicious code. We need to use a fixed SHA. |
| `githubactions:S6505` | `.github/workflows/build.yml:L26` | **Major** | By not using `--only-binary`, pip might download source code and run `setup.py`. This allows arbitrary code execution during the build process, which is a supply chain risk. |
| `githubactions:S6506` | `.github/workflows/build.yml:L27` | **Major** | If we don't lock versions (e.g., `pytest==7.4.4`), a future update could automatically install a broken or vulnerable version of the package without us knowing. |
| `python:S5754` | `src/library.py:L45` | **Critical** | A bare `except:` catches all errors, including system exits (like Ctrl+C). This hides real bugs and makes debugging almost impossible. We should catch specific exceptions like `ValueError`. |
| `python:S1192` | `src/library.py:L78` | **Major** | The exact same string literal (e.g., "Book not found") is written multiple times. If we need to change the message later, we might miss one, leading to inconsistent UI messages. |
| `python:S109` | `src/library.py:L112` | **Major** | Hardcoding magic numbers (like `14` for days late, or `5` for a fine) makes the code hard to maintain. It's better to use named constants like `MAX_LOAN_DAYS = 14`. |
| `python:S3776` | `src/library.py:L110` | **Major** | The function `process_checkout` has high cognitive complexity. It has too many nested `if/else` statements, making it hard for a developer to read, test, and maintain. |
| `python:S1481` | `src/library.py:L92` | **Minor** | An unused local variable (e.g., `temp_id`) was found. It clutters the code and might indicate a logic error where the developer forgot to use it. |

## Categorization
- **Blocker/Critical:** 2 (Bare except, Action SHA pinning)
- **Major:** 4 (Pip binary/locking, Duplicate strings, Magic numbers, Complex function)
- **Minor:** 1 (Unused variable)
- **Info:** 0 (None flagged yet)