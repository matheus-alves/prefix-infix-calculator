# Prefix and Infix Calculator

This repository contains a prefix (reverse polish) and infix notation calculator for a coding challenge.

### Requirements

- Python 3.8+

### Running locally

In order to run the API locally, use the following commands:

```
pip3 install -r requirements.txt
uvicorn api:app --reload
```

After this, you can access the user interface on http://127.0.0.1:8000

If you want to specify a different port you can use:

```
uvicorn api:app --reload --port <PORT>
```

### Unit tests

```
pip3 install pytest
cd tests
pytest
```

### Code checks

```
pip3 install mypy
pip3 install pylint

mypy calculator
pylint calculator
```

### Note:

- For the infix calculator, the internal python `eval` function could be used directly, but that defeats the purpose of 
the challenge :)