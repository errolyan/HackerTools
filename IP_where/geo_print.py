# -*- coding:utf-8 -*-
# /usr/bin/python
'''
-------------------------------------------------
   File Name   :  geo_print
   Description :  依据 GeoLiteCity 数据库， http://code.google.com/p/pygeoip/
   Envs        :  python == 3.55
                  pip install   dpkt geoip2
   Date        :  2021/3/2  下午2:50
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

import dpkt
import socket
import geoip2.database
import argparse


def ret_geo_str(ip):
    """ This function is not part of the original code of Violent
    Python. It used the deprecated 'pygeoip' library to perform
    the same task. A new solution using the API to the database
    provided by the MaxMind service has been implemented here by
    EONRaider. https://github.com/EONRaider"""

    try:
        with geoip2.database.Reader('geolite2_city.mmdb') as gi:
            rec = gi.city(ip)
            city = rec.city.name
            country = rec.country.name
            return '{}, {}'.format(city,country) if city else country

    except Exception as e:
        print('{"":>3}[-] Exception: {}'.format(e.__class__.__name__))
        return 'Unregistered'


def print_pcap(pcap_file):
    for ts, buf in pcap_file:
        try:
            eth = dpkt.ethernet.Ethernet(buf)
            ip = eth.data
            src = socket.inet_ntoa(ip.src)
            dst = socket.inet_ntoa(ip.dst)
            print('[+] Src: {} --> Dst: {}'.format(ret_geo_str(src),ret_geo_str(dst)))
        except Exception as e:
            print('{"":>3}[-] Exception: {}'.format(e.__class__.__name__))
            pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage='python3 geo_print PCAP_FILE')
    parser.add_argument('pcap', type=str, metavar='PCAP_FILE',
                        help='specify the name of the PCAP file')
    args = parser.parse_args()
    pcap = args.pcap

    with open(pcap, 'rb') as file:
        pcap = dpkt.pcap.Reader(file)
        print_pcap(pcap)


