import hmac
import hashlib
import base64

signature = hmac.new("zihua", '123456', digestmod=hashlib.sha256).digest()
print type(signature)


def toHex(str):
    lst = []
    for ch in str:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0' + hv
        lst.append(hv)
    return reduce(lambda x, y: x + y, lst)


print toHex(signature)

s = base64.b64encode(
    '9abdca03b15f2038d9fddf1311a78ccb5a46a58a8fc60340c8f3c792fcfa0a3e')
print s
print base64.b64decode(s)
