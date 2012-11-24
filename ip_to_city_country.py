#!/usr/bin/env python

import pygeoip
import argparse
import sys

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Show city and country of IP addresses using MaxMind GeoIP Database")
    parser.add_argument("-d", dest="geoipdb", help="Path to the GeoIPCity database (default: GeoLiteCity.dat)", default="GeoLiteCity.dat")
    parser.add_argument("ipfile", nargs='?', type=argparse.FileType('r'), 
        help="a file from which to read IP addresses (default: stdin)", default=sys.stdin)

    args = parser.parse_args()

    gi = pygeoip.GeoIP(args.geoipdb, pygeoip.MEMORY_CACHE)

    for ipaddr in args.ipfile:
        record = gi.record_by_addr(ipaddr)
        if record is None:
            sys.stdout.write("{}:<error>:<error>\n".format(ipaddr.strip()))
            continue

        for rt in ("country_code", "city"):
            if not record[rt].strip():
                record[rt] = "<unknown>"
                

        sys.stdout.write("{}:{country_code}:{city}\n".format(ipaddr.strip(), **record))
