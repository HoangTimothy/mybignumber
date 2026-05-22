Develop a simple function

## 1. Introduction

- Document name: Add2Num
- Project: Add 2 numbers
- Creator: Hoang Timothy

This project implements a core function that adds two large numbers represented as strings, using the same step-by-step method that students use in primary school.

The core logic is wrapped in a separate class named `MyBigNumber`, so another team can reuse it from a UI, console app, or a larger system.

## 2. Input

- The content in section 1 of the requirement document.

## 3. Preparation

- Python 3.13 or update
- `unittest` for unit testing
- Logging via the Python `logging` module

## 4. Request

The core code is implemented in [`src/add2num.py`](src/add2num.py).

The main class is `MyBigNumber`, with method `sum(stn1, stn2)`.

Implementation approach:

1. Scan both strings from right to left.
2. Read one digit from each string in each step.
3. Add two digits together with the current carry.
4. Store the current digit in the result and remember the new carry.
5. Repeat until both strings and the carry are exhausted.
6. Reverse the collected digits to get the final result string.

The method also records each arithmetic step by logging, so the addition process can be traced easily.

Where the logs appear:

- When you run [`src/add2num.py`](src/add2num.py), the demo configures `logging` to print INFO-level messages to the console.
- When you run the unit tests, the logs are captured by the test fixture in [`tests/unittest.py`](tests/unittest.py) and are asserted in memory instead of being printed.
- If you want to see the log stream while testing, run the module directly or attach a stream handler in your own script.

Example:

- `sum("1234", "897")` returns `2131`
- Step 1: `4 + 7 = 11`, write `1`, carry `1`
- Step 2: `3 + 9 + 1 = 13`, write `3`, carry `1`
- Continue the same way until all digits are processed.

Assumption used in this project:

- Input values are valid digit strings only.
- No invalid data handling is required for this task.

## 5. Output

Deliverables:

- Source code is stored in the Git repository.
- Unit tests are included in [`tests/unittest.py`](tests/unittest.py).```

## 6. Run

Run the unit tests:

```bash
python -m tests.unittest
```

Run the demo from the module directly:

```bash
python src/add2num.py
```

This prints the step-by-step addition log to the console.

## 7. Unit Testing

The repository includes unit tests for:

- simple addition
- carry propagation
- different length inputs
- leading zeros
- zero + zero
- logging output of each step
