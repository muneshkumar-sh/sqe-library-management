## Task 4: Coverage vs. Quality Discussion (The Coverage Trap)

**The Weak Test:** 
`test_valid_rating_is_accepted` was originally written with a weak assertion (`assert True` or simply calling the method without asserting the output). 

**Why it is a Coverage Trap:**
This test executes the `add_rating` method, meaning that line of code will show up as "covered" (green) in the HTML report. However, if a developer accidentally broke the `add_rating` method so that it didn't actually save the rating, this test would still pass. It gives a false sense of security because it measures *execution* rather than *verification*.

**The Fix:**
The test was strengthened by explicitly asserting `valid_book.rating == 4`. This ensures that the code not only runs without crashing, but also produces the correct side effect.