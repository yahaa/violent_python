import pygeoip
gi = pygeoip.GeoIP('Geo.dat')


def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    # print type(rec)
    for key in rec:
        print str(key)+': '+str(rec[key])
    # print rec
    # city = rec['city']
    # country = rec['country_name']
    # longitude = rec['longitude']
    # lat = rec['latitude']
    # print '[*] Target :' + tgt + ' Geo-located. '
    # print '[+] ' + str(city) + ', ' + str(country)
    # print '[+] Latitude: ' + str(lat) + ', Longitude: ' + str(longitude)
tgt = '115.29.146.79'
printRecord(tgt)
