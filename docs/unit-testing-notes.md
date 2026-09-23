# Unit Testing Notes

## Lab 07 — Library Management System

### Fixture Scopes

#### Function Scope

The default pytest fixture scope is `function`.

A function-scoped fixture creates a new fixture instance for every test that uses it.

In this project, function-scoped fixtures are used when tests need independent objects, such as a fresh `Book` or `Library`.

Example:

```python
@pytest.fixture
def library():
    return Library()