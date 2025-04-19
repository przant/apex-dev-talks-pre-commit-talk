# Sample Project with Pre-commit Hooks

This is a sample project that demonstrates the usage of pre-commit hooks.

## Intentional Errors

This project contains several intentional errors to trigger various pre-commit hooks:

1. Trailing whitespace (will be caught by `trailing-whitespace` hook)  
2. Missing executable permissions on scripts (will be caught by `check-shebang-scripts-are-executable`)
3. Invalid JSON format (will be caught by `check-json`)
4. Invalid YAML format (will be caught by `check-yaml`)
5. Missing newline at end of file (will be caught by `end-of-file-fixer`)
6. Usage of BOM in files (will be caught by `fix-byte-order-marker`)
7. Typos in code and comments (will be caught by `codespell`)
8. Missing type annotations (will be caught by `python-use-type-annotations`)

## Installation

1. Install pre-commit:
   ```
   pip install pre-commit
   ```

2. Install the pre-commit hooks:
   ```
   pre-commit install --hook-type pre-commit --hook-type commit-msg
   ```

3. Run pre-commit on all files:
   ```
   pre-commit run --all-files
   ```

## Usage

The project doesn't actually do anything useful - it's just meant to demonstrate pre-commit hooks!
