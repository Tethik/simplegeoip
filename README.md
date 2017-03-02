# simple-geoip
Dead simple geoip package. Basically a wrapper around maxminddb that downloads the database for you.

# Usage
As a python package.
```python
import simplegeoip

simplegeoip.lookup('127.0.0.1')
```

As a standalone script
```bash
python simplegeoip.py 8.8.8.8
```
