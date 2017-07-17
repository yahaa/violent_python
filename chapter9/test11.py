def addx(x):
    def adder(y): return x + y
    return adder


c = addx(18)
print c
print c.__closure__
print c(10)


def dobi(f):
    return f()


@addx
def go():
    print 'gggggggooooo'


print '666666666666666'


def makebold(fn):
    def w():
        return "<b>" + fn() + "</b>"
    return w


def make2(fn):
    def w2():
        return "<i>" + fn() + "</i>"
    return w2


@make2
def hello():
    print 'hello world !'


hello()
