name = 'zihua{}'
email = 'yuanzihua@gmail.com'
password = '123456'
phone = '18777859598'
pic = 'default'
for i in range(1, 10):
    print 'insert into user value ("{}","{}",md5({}),"{}","{}");'.format(name.format(i), email, password, phone, pic)
