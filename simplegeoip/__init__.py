import os
import gzip
import shutil
import sys
import logging
import tempfile
import time
import maxminddb
import requests
from appdirs import site_data_dir, user_data_dir

__title__ = "simplegeoip"

DATABASE = 'GeoLite2-City.mmdb'
MAXMIND_GEOLITE_URL = 'https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz'

def _ensure_dir_exists(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        return directory
    except:
        return None

def database_path():
    directory = _ensure_dir_exists(site_data_dir(__title__)) or \
                _ensure_dir_exists(user_data_dir(__title__))
    if not directory:
        raise EnvironmentError("Could not find a suitable data directory.")
    return os.path.join(directory, DATABASE)

def reader():
    if not os.path.exists(database_path()):
        logging.info("The Geolite database is not installed. Proceeding to download it.")
        download_latest_database()
    _reader = maxminddb.open_database(database_path())
    return _reader

MAXMINDDB_READER = None
def lookup(ip):
    global MAXMINDDB_READER
    if MAXMINDDB_READER is None:
        MAXMINDDB_READER = reader()
    return MAXMINDDB_READER.get(ip)

def last_updated():
    secs = reader().metadata().build_epoch
    _time = time.gmtime(secs)
    return "Geolite database was last updated: " + time.strftime("%c", _time)

def download_latest_database():
    with tempfile.NamedTemporaryFile() as tmpfile:
        resp = requests.get(MAXMIND_GEOLITE_URL, stream=True)

        for chunk in resp.iter_content(chunk_size=1024):
            tmpfile.write(chunk)
        tmpfile.flush()

        logging.info("Geolite Database downloaded to " + tmpfile.name)

        with gzip.open(tmpfile.name, 'rb') as f_in:
            with open(database_path(), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

        logging.info("Geolite Database successfully decrompessed and saved to %s. " + \
                     "Ready for use.", database_path())
