import pcap
import dpkt
import pygeoip
gi = pygeoip.GeoIP('Geo.dat')


def capPack(pc):
    kmlPts = ''
    ct = 0
    for ptime, pdata in pc:
        try:
            if ct >= 100:
                break
            p = dpkt.ethernet.Ethernet(pdata)
            if p.data.__class__.__name__ == 'IP':
                ipsrc = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.src)))
                ipdst = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.dst)))
                srckml = retKML(ipsrc)
                dstkml = retKML(ipdst)
                kmlPts = kmlPts + srckml + dstkml
                ct += 1
        # src = getDetail(str(ipsrc))
        # dst = getDetail(str(ipdst))
        # print ipsrc, ' to ', ipdst
        # print src, ' to ', dst, '\n\n
        except Exception, e:
            pass
    return kmlPts


def retKML(ip):
    rec = gi.record_by_name(ip)
    try:
        longitude = rec['longitude']
        latitude = rec['latitude']
        kml = (
            '<Placemark>\n'
            '<name>%s</name>\n'
            '<Point>\n'
            '<coordinates>%6f,%6f</coordinates>\n'
            '</Point>\n'
            '</Placemark>\n'
        ) % (ip, longitude, latitude)
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
        # print retKML('115.29.146.79')
    main()
