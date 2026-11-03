# Calculator App

A simple Python calculator application that performs basic arithmetic operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Input-driven calculator menu
- Division rounded to two decimal places
- Zero-division safety message

## Project Structure

- `calculator.py` contains the arithmetic functions
- `main.py` contains the interactive CLI menu
- `tests/test_calculator.py` contains automated tests

## Getting Started

### Prerequisites

- Python 3 installed

### Run the application

From the project root, run:

```bash
python main.py
```

## Usage

1. Run the script.
2. Enter the first number.
3. Enter the second number.
4. Choose an operation from the menu.
5. View the result.

### Example

- Addition: `5 + 3 = 8`
- Subtraction: `5 - 3 = 2`
- Multiplication: `5 * 3 = 15`
- Division: `10 / 4 = 2.5`

## Testing

Run the test suite with:

```bash
python -m pytest -q
```

The project currently includes tests covering:

- addition
- subtraction
- multiplication
- division
- division-by-zero handling

## Project Status

The calculator supports the core four arithmetic operations and includes automated tests.

## Version History

### v1.1.0

- Added multiplication support
- Added division support
- Rounded division output to two decimal places
- Added automated tests for calculator functions

### v1.0.0

- Initial calculator project
- Added addition and subtraction

## Contributing

Suggestions and improvements are welcome.

## License

No license has been specified yet.
