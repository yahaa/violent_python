# encoding=utf-8
from mongoengine import *
connect('test_engine')


class User(Document):
