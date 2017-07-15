import sys
import httplib


soap = '''
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CheckUserLogin xmlns="www.lib.shu.edu.cn">
      <UserID>{}</UserID>
      <password>{}</password>
    </CheckUserLogin>
  </soap:Body>
</soap:Envelope>
'''.format('11223344', '11223344')


webservice = httplib.HTTP('202.120.121.204:8888')
webservice.putrequest('POST', '/WebService/shulibLogin.asmx HTTP/1.1')

webservice.putheader('Host', '202.120.121.204:8888')
webservice.putheader('Content-Type', 'text/xml; charset=utf-8')
webservice.putheader(
    "User-Agent", "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)")
webservice.putheader('Content-Length', len(soap))
webservice.putheader('SOAPAction', 'www.lib.shu.edu.cn/CheckUserLogin')
webservice.endheaders()
webservice.send(soap)

statuscode, statusmessage, header = webservice.getreply()
print "Response: ", statuscode, statusmessage
print "headers: ", header
res = webservice.getfile().read()
print res


t = '''
POST /WebService/shulibLogin.asmx HTTP/1.1
Host: 202.120.121.204
Content-Type: text/xml; charset=utf-8
Content-Length: length
SOAPAction: "www.lib.shu.edu.cn/CheckUserLogin"
'''
