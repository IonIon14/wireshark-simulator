#!/usr/bin/python
import os
import sys
from scapy.all import *

import json
from caption import *
class Pachete():
    def __init__(self,ETH_dst,ETH_src,IP_src,IP_dst,IP_version,IP_proto,TCP_sport,TCP_dport,UDP_sport,UDP_dport):
        self.ETH_dst=ETH_dst
        self.ETH_src = ETH_src
        self.IP_src = IP_src
        self.IP_dst = IP_dst
        self.IP_version =IP_version
        self.IP_proto = IP_proto
        self.TCP_sport = TCP_sport
        self.TCP_dport = TCP_dport
        self.UDP_sport = UDP_sport
        self.UDP_dport = UDP_dport
    def __str__(self):
        json_string='{{"Ethernet":{{"src":"{}","dst":"{}"}},"IP":{{"src":"{}","dst":"{}","version":"{}","proto":"{}"}},"TCP":{{"sport":"{}","dport":"{}"}},"UDP":{{"sport":"{}","dport":"{}"}}}}'.format(self.ETH_src,self.ETH_dst,self.IP_src,self.IP_dst,self.IP_version,self.IP_proto,self.TCP_sport,self.TCP_dport,self.UDP_sport,self.UDP_dport)
        json_object=json.loads(json_string)
        json_formatted_str=json.dumps(json_object,indent=2)
        return json_formatted_str



