def log(func):
    def wra(*args, **kw):
        print "call %s()" % func.__name__
        return func(*args, **kw)
    return wra


def now():
    print "2017-6-4"


now = log(now)
