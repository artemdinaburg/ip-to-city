ip-to-city
==========

Map an IP address to City/Country via the MaxMind GeoLite database


## Usage ##

>>> $ ./ip_to_city_country.py --help
usage: ip_to_city_country.py [-h] [-d GEOIPDB] [ipfile]

Show city and country of IP addresses using MaxMind GeoIP Database

positional arguments:
  ipfile      a file from which to read IP addresses (default: stdin)

  optional arguments:
    -h, --help  show this help message and exit
    -d GEOIPDB  Path to the GeoIPCity database (default: GeoLiteCity.dat)


>>> $ echo '8.8.8.8' | ./ip_to_city_country.py
8.8.8.8:US:Mountain View

