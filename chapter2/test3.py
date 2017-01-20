# -*- coding: UTF-8 -*-
class Student:
	count = 0
	books = []

    def __init__(self,name,age):
    	self.name=name
    	self.age=age
    pass



    def __ttt__(self, n):
        res = 0
        for i in range(n):
            res += i
        return res

    @staticmethod
    def tit(n):
        res = 0
        for i in range(n):
            res += i
        return res

    
print Student.tit(10)

