# ST211 Automated Software Testing

This repository contains class exercises and testing activities for the ST211 Automated Software Testing course.

## Projects

### Roman Numeral Converter

The [`Roman`](Roman/) folder contains a Roman numeral converter that:

- Converts Roman numerals to integers
- Converts integers to Roman numerals
- Accepts lowercase Roman numerals
- Validates standard Roman numeral formatting
- Rejects invalid characters, repetitions, subtraction patterns, and values outside 1 to 3999

See the [Roman README](Roman/README.md) for details.

### Class Exercises

The [`Class-Exercises`](Class-Exercises/) folder contains introductory testing exercises for:

- Bank account deposits and withdrawals
- Letter-grade calculation
- Boundary and behavior testing with `pytest`

See the [Class Exercises README](Class-Exercises/README.md) for setup and test details.

## Requirements

- Python 3.8 or newer
- `pytest`

Install the testing dependency with:

```bash
python -m pip install pytest
```

## Running All Tests

From the repository root, run:

```bash
python -m pytest st211-quizzes-6705140023
```

To run a specific project:

```bash
python -m pytest st211-quizzes-6705140023/Roman
python -m pytest st211-quizzes-6705140023/Class-Exercises
```

## Test Status

The Roman numeral test suite currently passes all 24 tests. The Class Exercises suite currently contains 9 tests, with 7 passing and 2 failing because of existing incorrect expected balances in the test files.