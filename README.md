# simple-geoip
Dead simple geoip package. Pretty much just a wrapper around [maxminddb](https://github.com/maxmind/MaxMind-DB-Reader-python/) 
that automatically downloads the geolite database for you. You can either do this manually using the 'download_latest_database_from_maxmind' function 
or let the script do it automatically when it detects no database is installed.

Can be used as a package or standalone script.

# Usage
As a python package.
```python
import simplegeoip

# Gets a dict with country/city information 
simplegeoip.lookup('127.0.0.1')
# Downloads an updated database into simplegeoip's package directory
simplegeoip.download_latest_database_from_maxmind()
# Tells you when the database was last updated by maxmind
simplegeoip.last_updated()
```

The same as above but as a standalone script
```bash
simplegeoip 8.8.8.8
simplegeoip update
simplegeoip info 
```
