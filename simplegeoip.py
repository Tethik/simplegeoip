import maxminddb
import requests
import os
import gzip
import shutil
import sys

DATABASE = 'db/GeoLite2-City.mmdb'
MAXMIND_GEOLITE_URL = 'https://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz'

_reader = None
def lookup(ip):
    global _reader
    if _reader is None:
        if not os.path.exists(DATABASE):
            download_latest_database_from_maxmind()
        _reader = maxminddb.open_database(DATABASE)
    return _reader.get(ip)

def download_latest_database_from_maxmind():
    dir = os.path.dirname(os.path.abspath(__file__))
    local_filename = os.path.join(dir, DATABASE+'.gz')
    r = requests.get(MAXMIND_GEOLITE_URL, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: 
                f.write(chunk)
            
    with open(DATABASE, 'wb') as f_out:
        with gzip.open(local_filename, 'rb') as f_in:
            shutil.copyfileobj(f_in, f_out)

    return local_filename

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: ")
        exit(0)
    
    if sys.argv[1].strip() == "update":
        download_latest_database_from_maxmind()
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
    

    