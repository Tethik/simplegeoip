import maxminddb
import requests
import os
import gzip
import shutil
import sys
import logging
import tempfile
import time

DATABASE = 'db/GeoLite2-City.mmdb'
MAXMIND_GEOLITE_URL = 'https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz'

def package_path():
    return os.path.dirname(os.path.abspath(__file__))

def database_path():
    return os.path.join(package_path(), DATABASE)

_reader = None
def reader():
    global _reader
    if _reader is None:
        if not os.path.exists(database_path()):
            download_latest_database_from_maxmind()
        _reader = maxminddb.open_database(database_path())
    return _reader

def lookup(ip):    
    return reader().get(ip)

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

        logging.info("Geolite Database successfully decrompessed and saved. Ready for use.")

logging.basicConfig(level=logging.INFO)

def main():
    if len(sys.argv) < 2:
        print("""USAGE: {binary} [update] <ip, ip2, ...>

        {binary} update
            Downloads a new version of the maxmind geolite database.

        {binary} <ip, ip2, ....>
            Performs lookups for each argument given and prints the results.

        {binary} info
        """)
        exit(0)
    
    if sys.argv[1].strip() == "update":
        download_latest_database_from_maxmind()
        exit(0)

    if sys.argv[1].strip() == "info":
        print(last_updated())
        exit(0)

    for arg in sys.argv[1:]:
        ip = arg.strip()
        result = lookup(ip)
        if 'country' in result:
            country = result['country']['names']['en']            
            if 'city' in result:
                city = result['city']['names']['en']
                print("{ip}: {country}, {city}".format(ip=ip, country=country, city=city))
            else:
                print("{ip}: {country}".format(ip=ip, country=country))
        else:
            print("{ip}: Nothing found.".format(ip=ip))
    
if __name__ == "__main__":
    main()

    