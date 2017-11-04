#!usr/bin/env python3
#coding=utf-8
#author=Gullom

#a = -100
#if a >= 0:
#    print(a)
#else:
#    print(-a)


#!usr/bin/env python
#coding=utf-8
#print(r'I\'m \"ok\"as\td')

#字符串即包含 ‘ 又包含 “ 用 \ 隔开    \'

#print('''line1\\
#line2
#line3''')



#print(3>2)


#name = input()
#print(name)

#n = 123
#f = 456.789
#s1 = 'hello,word'
#s2 = 'hello,\'Adam\''
#s3 = r'hello,"Bart"'
#s4 = r'''hello,
#Lisa!'''
#print('n=',n,'\nf=',f,'\ns1=',s1,'\ns2=',s2,'s3=',s3,'\ns4=',s4)
# TODO 学习了


x = 10
x = x+10
#print(x)

a='ABC'
b = a
a = 'RTY'
#print(b)


I=ord('H')
print(I)

w=chr(32534)
print(w)

Y = len('岁的法国'.encode('utf-8'))
print(Y)


#!usr/bin/env python3
# coding=utf-8

z = 75
x = 85
c = (x-z)/z*100
print('%.1f%%' % c)


p = '%02d-%003d' % (4,2)
print(p)


p = '%.3f' % 2.3333
print(p)

s = 'Python-中文'
print(s)
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))