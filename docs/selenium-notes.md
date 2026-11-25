# Lab 13 – Task 3: Explicit Waits Practice

## Objective

To compare Selenium explicit waits with fixed sleep when testing asynchronous API operations under simulated network latency.

## Experimental Setup

- Application: LibraryHub
- Testing framework: Selenium WebDriver and pytest
- Browser: Google Chrome
- Artificial API delay: 1 second
- Endpoint: POST /members/501/borrow
- Explicit wait timeout: 10 seconds
- Fixed sleep duration: 0.2 seconds
- Number of runs per approach: 5

## Methodology

A one-second artificial delay was introduced into the borrow API endpoint using `time.sleep(1)`.

A book containing two available copies was added to the catalog. The borrow operation was performed, and the test verified whether the available copies decreased from two to one.

Two approaches were tested:

1. Explicit wait using WebDriverWait and expected conditions.
2. Fixed sleep using time.sleep(0.2).

## Experimental Results

| Run | Explicit Wait | Fixed Sleep |
|---|---|---|
| 1 | PASS | FAIL |
| 2 | PASS | FAIL |
| 3 | PASS | FAIL |
| 4 | PASS | FAIL |
| 5 | PASS | FAIL |
| Total Passed | 5 | 0 |
| Total Failed | 0 | 5 |
| Success Rate | 100% | 0% |

## Observations

The explicit wait successfully waited until the available copies decreased from two to one.

The fixed-sleep approach failed in all five runs because the 0.2-second waiting period was insufficient for the delayed API operation.

The fixed-sleep tests produced the following assertion error:

`AssertionError: assert '2' == '1'`

An earlier explicit-wait experiment produced four passes and one timeout failure. The test was improved by confirming that the book existed before borrowing and increasing the explicit wait timeout to ten seconds.

Connection errors and coding errors encountered during setup were excluded from the final experimental results because they did not measure synchronization behavior.

## Conclusion

Explicit waits are more reliable than fixed sleeps for testing asynchronous web applications. They wait until a specific condition is satisfied instead of relying on a predetermined delay.

The experiment demonstrated a 100% success rate for the corrected explicit-wait approach and a 0% success rate for the fixed-sleep approach. Under the configured latency, fixed-sleep failures were consistent rather than intermittent.

Therefore, explicit waits are preferred for reliable Selenium test automation.