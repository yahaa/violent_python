import os


class Test(object):
    def m1(self, *args):
        print args

    def parse(self):
        a = ['a', 'b', 'c', 'd']
        b = ['bb', 'cc', 'dd']
        return a, b

    def show(self):
        self.m1(*self.parse())


test = Test()

test.show()


web:
    build: .
    command:
        python app.py
    ports: - "5000:5000"
    volumes: -.: / code
    links: -
        redis
redis:
    image:
        redis
