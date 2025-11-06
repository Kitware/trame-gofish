# trame-gofish

Trame widget for GoFish chart library that can be found at
https://gofish.graphics/

[Demo](https://raw.githubusercontent.com/Kitware/trame-gofish/refs/heads/main/trame-gofish.png)

```
uv run https://raw.githubusercontent.com/Kitware/trame-gofish/refs/heads/main/examples/tuto-final.py
```

## License

This library is OpenSource and follow the MIT License

## Installation

Install the application/library

```sh
pip install trame-gofish
```

## Development setup

We recommend using uv for setting up and managing a virtual environment for your
development.

```sh
# Create venv and install all dependencies
uv sync --all-extras --dev

# Activate environment
source .venv/bin/activate

# Install commit analysis
pre-commit install
pre-commit install --hook-type commit-msg

# Allow live code edit
uv pip install -e .
```

Build and install the Vue components

```sh
cd vue-components
npm i
npm run build
cd -
```

For running tests and checks, you can run `nox`.

```sh
# run all
nox

# lint
nox -s lint

# tests
nox -s tests
```

## Professional Support

- `Training <https://www.kitware.com/courses/trame/>`\_: Learn how to
  confidently use trame from the expert developers at Kitware.
- `Support <https://www.kitware.com/trame/support/>`\_: Our experts can assist
  your team as you build your web application and establish in-house expertise.
- `Custom Development <https://www.kitware.com/trame/support/>`\_: Leverage
  Kitware’s 25+ years of experience to quickly build your web application.
