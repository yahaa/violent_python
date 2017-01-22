from scapy.all import *


def testTTL(ptk):
    try:
        if pkt.haslayer(IP):
            ipsrc = pkt.getlayer(IP).src
            ttl = str(ptk.ttl)
            print '[+] Pkt received From : ' + ipsrc + ' with TTL' + ttl
    except:
        pass


def main():
    sniff(prn=testTTL, store=0)

if __name__ == '__main__':
    main()
