# coding=utf-8
sql = 'insert into User(uId,email,phone,sex,uName,uPwd) value("%s","%s","%s","%s","%s",md5(%s));'
name = 'zihua'
email = 'zihua@qq.com'
sex = '男'
phone = '18777859598'

for i in range(100):
    print sql % (name + str(i), email, phone, sex, name, '123456')
