# Roman Numeral Converter

This project implements Roman numeral conversion and validation in Python. It supports standard Roman numerals representing values from 1 to 3999.

## Features

- Convert Roman numerals to integers with `roman_to_integer()`
- Convert integers to Roman numerals with `integer_to_roman()`
- Accept lowercase Roman numeral input
- Support standard subtractive notation such as `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`
- Reject invalid characters, repeated symbols, invalid subtraction pairs, non-canonical formats, and out-of-range values
- Run the converter interactively from the command line

## Files

| File | Description |
| --- | --- |
| `roman.py` | Roman numeral conversion functions and interactive CLI. |
| `test_roman.py` | Automated tests for conversions and invalid input handling. |

## Requirements

- Python 3.8 or newer
- `pytest`

Install `pytest` with:

```bash
python -m pip install pytest
```

## Usage

From this folder, import and use the conversion functions:

```python
from roman import integer_to_roman, roman_to_integer

print(integer_to_roman(2026))  # MMXXVI
print(roman_to_integer("MMXXVI"))  # 2026
```

To start the interactive converter:

```bash
python roman.py
```

## Running Tests

From the repository root, run:

```bash
python -m pytest st211-quizzes-6705140023/Roman
```

The current test suite contains 24 tests covering valid conversions, lowercase input, boundary values, and invalid Roman numeral formats.
