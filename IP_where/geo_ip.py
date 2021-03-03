# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  geo_ip
   Description :  使用 PyGeoIP 关联 IP 地址到物理地址
   Envs        :  python == 3.66
                  pip install  geoip2
   Date        :  2021/3/2  下午2:59
   CodeStyle   :  规范,简洁,易懂,可阅读,可维护,可移植!
-------------------------------------------------
   Change Activity:
          2021/3/2 : build
-------------------------------------------------
__Author__ = "Yan Errol 13075851954"
__Email__ = "260187357@qq.com"
__Copyright__ = "Copyright 2021, Yan Errol"
-------------------------------------------------
'''
import argparse
import geoip2.database


def print_record(target_ip):
    """ This function is not part of the original code of Violent
    Python. It used the deprecated 'pygeoip' library to perform
    the same task. A new solution using the API to the database
    provided by the MaxMind service has been implemented here by
    EONRaider. https://github.com/EONRaider"""

    with geoip2.database.Reader('geolite2_city.mmdb') as gi:
        rec = gi.city(target_ip)
        city = rec.city.name
        region = rec.subdivisions.most_specific.name
        country = rec.country.name
        lat = rec.location.latitude
        long = rec.location.longitude
        print('[*] Target: {} Geo-located.'.format(target_ip))
        print('[+] {}, {}, {}'.format(city,region,country))
        print('[+] Latitude: {}, Longitude: {}'.format(lat,long))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        usage='python3 geo_ip.py TARGET_IP')
    parser.add_argument('tgt_ip', type=str, metavar='TARGET_IP',
                        help='IP address of the target to geolocate')

    print_record(parser.parse_args().tgt_ip)

'''
python3 geo_ip.py 36.152.44.9
'''