import pcap
import dpkt
import pygeoip
gi = pygeoip.GeoIP('Geo.dat')


def capPack(pc):
    kmlLts = ''
    ct = 0
    for ptime, pdata in pc:
        try:
            if ct >= 10:
                break
            p = dpkt.ethernet.Ethernet(pdata)
            if p.data.__class__.__name__ == 'IP':
                ipsrc = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.src)))
                ipdst = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.dst)))
                kmlLts = kmlLts + retKML(ipsrc, ipdst)
                ct += 1

        except Exception, e:
            pass
    return kmlLts


def retKML(ip1, ip2):
    rec1 = gi.record_by_name(ip1)
    rec2 = gi.record_by_name(ip2)
    try:
        longitude1 = rec1['longitude']
        latitude1 = rec1['latitude']
        longitude2 = rec2['longitude']
        latitude2 = rec2['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s to %s</name>\n'
            '<LineString>\n'
            '<coordinates>%6f,%6f,%6f,%6f</coordinates>\n'
            '</LineString>\n'
            '</Placemark>\n'
        ) % (ip1, ip2, longitude1, latitude1, longitude2, latitude2)

        return kml
    except Exception, e:
        return ''


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
    kmlheader = '<?xml version="1.0" encoding="UTF-8"?>'\
        '\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n'
    kmlfooter = '</Document>\n</kml>\n'
    print kmlheader + capPack(pc) + kmlfooter

if __name__ == '__main__':
    # print retKML('115.29.146.79', '115.29.146.220')
    main()
