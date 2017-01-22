import dpkt
import pcap


def findDownload(pcap):
    for ts, data in pcap:
        try:
            p = dpkt.ethernet.Ethernet(data)
            src = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.src)))
            tcp = p.data.data
            http = dpkt.http.Request(tcp.data)
            if http.method == 'GET':
                uri = http.uri.lower()
                if '.zip' in uri and 'loic' in uri:
                    print '[!] ' + src + ' Downloaded LOIC.'
        except:
            pass

pc = pcap.pcap('wlan0')
pc.setfilter('tcp port 80')
findDownload(pc)
