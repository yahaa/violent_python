from scapy.all import *


def pktPrint(pkt):
    if pkt.haslayer(Dot11Beacon):
        print '[+] Detected 802.11 Probe Request Frame'
    elif pkt.haslayer(TCP):
        print '[+] Detected a Tcp Packet'
    elif pkt.haslayer(DNS):
        print '[+] Detected a DNS Packet'
conf.iface = 'wlan0'
sniff(prn=pktPrint)

