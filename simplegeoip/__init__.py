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

def _ensure_dir_exists(dir):
    try:
        if not os.path.exists(dir):
            os.makedirs(dir)
        return dir
    except:
        return None

def database_path():
    d = _ensure_dir_exists(site_data_dir(__title__)) or _ensure_dir_exists(user_data_dir(__title__))
    if not d:
        raise EnvironmentError("Could not find a suitable data directory.")
    return os.path.join(d, DATABASE)


def reader():              
    if not os.path.exists(database_path()):
        logging.info("The Geolite database is not installed. Proceeding to download it.")
        download_latest_database_from_maxmind()
    _reader = maxminddb.open_database(database_path())
    return _reader

_reader = None
def lookup(ip):    
    global _reader
    if _reader is None: 
        _reader = reader()
    return _reader.get(ip)

def last_updated():
    secs = reader().metadata().build_epoch
    tm = time.gmtime(secs)
    return "Geolite database was last updated: " + time.strftime("%c", tm)

def download_latest_database_from_maxmind():    
    with tempfile.NamedTemporaryFile() as tmpfile:
        r = requests.get(MAXMIND_GEOLITE_URL, stream=True)      
        
        numbytes = 0
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: 
                tmpfile.write(chunk)
        tmpfile.flush()

        logging.info("Geolite Database downloaded to " + tmpfile.name)

        with gzip.open(tmpfile.name, 'rb') as f_in:
            with open(database_path(), 'wb') as f_out:            
                shutil.copyfileobj(f_in, f_out)

        logging.info("Geolite Database successfully decrompessed and saved to {}. Ready for use.".format(database_path()))



