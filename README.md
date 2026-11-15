# Calculator API

![CI](https://github.com/salmanpattupara/calculator/actions/workflows/ci.yml/badge.svg?branch=main)
![Release](https://img.shields.io/github/v/release/salmanpattupara/calculator)
![Python](https://img.shields.io/badge/python-3.12-blue)
![pytest](https://img.shields.io/badge/tested%20with-pytest-0A9EDC)

A simple calculator exposed as a web API with [FastAPI](https://fastapi.tiangolo.com/). The project was built to learn CI/CD: every push to `main` and every pull request runs the automated tests with coverage on GitHub Actions.

## Features

- Addition, subtraction, multiplication and division over HTTP
- Interactive API documentation generated automatically at `/docs`
- Input validation and clear error responses
- Automated tests for both the calculator logic and the API
- CI pipeline with test coverage reporting

## Getting started

### Prerequisites

- Python 3.12 or later
- Git

### Installation

```bash
git clone https://github.com/salmanpattupara/calculator.git
cd calculator
pip install -r requirements.txt
```

### Run the API

```bash
uvicorn main:app --reload
```

The server starts at http://127.0.0.1:8000. Open http://127.0.0.1:8000/docs to try every endpoint from the browser.

### Run with Docker

The Docker image is available on [GitHub Container Registry](https://github.com/salmanpattupara/calculator/pkgs/container/calculator).

Pull the image:

```bash
docker pull ghcr.io/salmanpattupara/calculator:695d1c4eb39f2328aa27740ebdf82c6e68edb5da
```

Run the API container:

```bash
docker run --name calculator-api -p 8000:8000 ghcr.io/salmanpattupara/calculator:695d1c4eb39f2328aa27740ebdf82c6e68edb5da
```

The API is then available at http://localhost:8000, with interactive documentation at http://localhost:8000/docs.

## API reference

All endpoints use `GET` with query parameters `a` and `b` (numbers).

| Endpoint | Example | Response |
|---|---|---|
| `/` | `/` | `{"message": "Calculator API is running"}` |
| `/add` | `/add?a=4&b=3` | `{"result": 7.0}` |
| `/subtract` | `/subtract?a=5&b=3` | `{"result": 2.0}` |
| `/multiply` | `/multiply?a=4&b=3` | `{"result": 12.0}` |
| `/divide` | `/divide?a=10&b=2` | `{"result": 5.0}` |

### Example request

```bash
curl "http://127.0.0.1:8000/add?a=4&b=3"
```

```json
{"result": 7.0}
```

### Errors

| Case | Status | Response |
|---|---|---|
| Division by zero, e.g. `/divide?a=10&b=0` | `400` | `{"detail": "Cannot divide by zero"}` |
| Non-numeric input, e.g. `/add?a=abc&b=3` | `422` | Validation error details |

## Running the tests

```bash
python -m pytest
```

With coverage:

```bash
python -m pytest --cov=calculator --cov=main --cov-report=term-missing
```

The `Missing` column in the coverage table lists the lines that no test runs.

## Project structure

```
calculator/
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions pipeline
├── tests/
│   ├── test_calculator.py    # tests for the calculator functions
│   └── test_api.py           # tests for the API endpoints
├── calculator.py             # calculator logic
├── main.py                   # FastAPI application
├── user_app.py               # deprecated user-input version
├── requirements.txt
└── README.md
```

## CI/CD

The workflow in `.github/workflows/ci.yml` runs on every push to `main` and on every pull request. It:

1. Checks out the code
2. Sets up Python 3.12
3. Installs the dependencies from `requirements.txt`
4. Runs all tests with coverage

## Contributing

1. Create a branch from an up-to-date `main`:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b my-change
   ```
2. Make your change and add or update tests.
3. Run `python -m pytest` locally.
4. Push the branch and open a pull request. Use `Closes #<issue-number>` in the description to link an issue.
5. Merge once the CI check is green.

## Versioning and releases

This project follows [semantic versioning](https://semver.org/): `MAJOR.MINOR.PATCH`. See the [Releases page](https://github.com/salmanpattupara/calculator/releases) for the full version history and release notes.

## Deprecated

The user-input version of the calculator (`user_app.py`) is deprecated and will be removed in a future release. The API is the only supported way to use the calculator going forward.

## License

No license has been added yet. If you want others to be able to reuse this code, add a `LICENSE` file (for example, MIT) to the repository.
