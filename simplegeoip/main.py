import logging
import sys
from simplegeoip import *

def main(args=None):    
    logging.basicConfig(level=logging.INFO)
    
    if args is None:
        args = sys.argv
    
    if len(args) < 2:
        print("""USAGE: {binary} [update] <ip, ip2, ...>

        {binary} update
            Downloads a new version of the maxmind geolite database.

        {binary} <ip, ip2, ....>
            Performs lookups for each argument given and prints the results.

        {binary} info
        """.format(binary=args[0]))
        return

    if args[1].strip() == "update":
        download_latest_database_from_maxmind()
        return 

    if args[1].strip() == "info":
        print(last_updated())
        return

    for arg in args[1:]:
        ip = arg.strip()
        try:
            result = lookup(ip)
            if result and 'country' in result:
                country = result['country']['names']['en']            
                if 'city' in result:
                    city = result['city']['names']['en']
                    print("{ip}: {country}, {city}".format(ip=ip, country=country, city=city))
                else:
                    print("{ip}: {country}".format(ip=ip, country=country))
            else:
                print("{ip}: Nothing found.".format(ip=ip))
        except ValueError as ex:
            print(ex)

if __name__ == "__main__":
    main()