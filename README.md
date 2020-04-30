# flake8-tuple-unpack-limit
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-tuple-unpack-limit)


An extension for flake8 to report on too long tuple unpacking.

Default max unpack length is 4 and can be configured
via `--max-unpack-length` option.

## Installation

    pip install flake8-tuple-unpack-length


## Example

Sample file:

```python
# test.py
def foo():
    return (1, 2, 3, 4, 5)


a, b, c, d, e = foo()
```

Usage:

```terminal
$ flake8 --max-unpack-length 3 test.py
test.py:6:1: TUL001 unpack too many variables (5 > 3)
```
