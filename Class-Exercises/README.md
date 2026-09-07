# Class Exercises

This folder contains Python exercises for practicing automated software testing with `pytest`.

## Contents

| File | Description |
| --- | --- |
| `bank.py` | Implements a simple `BankAccount` with deposit and withdrawal operations. |
| `grades.py` | Converts a score from 0 to 100 into a letter grade. |
| `test_bank.py` | Tests deposits, withdrawals, and multiple account operations. |
| `test_depedent.py` | Additional bank account test cases. |
| `test_grades.py` | Tests grade boundaries and valid score limits. |

## Requirements

- Python 3.8 or newer
- `pytest`

Install `pytest` with:

```bash
python -m pip install pytest
```

## Running the Tests

From the repository root, run:

```bash
python -m pytest st211-quizzes-6705140023/Class-Exercises
```

Or run the tests from inside this folder:

```bash
python -m pytest
```

## Current Test Status

The current suite contains 9 tests. At the time this README was written, 7 tests passed and 2 tests failed because their expected balances do not match the implemented deposit and withdrawal calculations. The failing expectations are in `test_bank.py` and `test_depedent.py`.
