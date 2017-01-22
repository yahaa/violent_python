import pcap
import dpkt
import pygeoip
gi = pygeoip.GeoIP('Geo.dat')


def capPack(pc):
    for ptime, pdata in pc:
        try:
            p = dpkt.ethernet.Ethernet(pdata)
            if p.data.__class__.__name__ == 'IP':
                ipsrc = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.src)))
                ipdst = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.dst)))
                src = getDetail(str(ipsrc))
                dst = getDetail(str(ipdst))
                print ipsrc, ' to ', ipdst
                print src, ' to ', dst,'\n\n'
        except:
            pass


def getDetail(tgt):
    try:
        rec = gi.record_by_name(tgt)
        city = rec['city']
        country = rec['country_code3']
        if city != '':
            geoloc = city + ', ' + country
        else:
            geoloc = country
        return geoloc
    except Exception, e:
        return 'Unreg'


def main():
    pc = pcap.pcap('wlan0')
    pc.setfilter('tcp port 80')
    capPack(pc)

if __name__ == '__main__':
    main()
