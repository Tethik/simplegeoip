# Development cheatsheet

Everything that follows assumes that you are in a virtualenv.

# Testing

```
pytest
```

With coverage

```
pytest --cov --cov-report=term-missing
```

# Linting

```
python $(which pylint) simplegeoip
```

# PYPI

Upload a new version like this:

```
python setup.py sdist bdist_wheel upload
```
