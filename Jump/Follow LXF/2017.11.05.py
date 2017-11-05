#!usr/bin/env python3
#coding=utf-8

# list  tuple

L = [
    ['Apple','Google','Microsoft'],
    ['Java','Python','Rudy','PHP'],
    ['Adam','Bart','Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

#  条件判断

age = 19
if age >= 18:
    print('your age is',age)
    print('adult')


age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('kid')


# input()返回的数据类型是str,str不能直接和整数比较，必须把str转换成整数

s = input('birth:')
birth = int(s)
if birth < 2000 :
    print('00前')
else :
    print('00后')



height = 1.75
weight = 85.5
BMI = int( weight / height /height )
if BMI <18.5:
    print('过轻')
elif BMI <25:
    print('正常')
elif BMI <28:
    print('过重')
elif BMI <32:
    print('肥胖')
else:
    print('严重肥胖')

i = 2
if i == 2:
    print(i)



# 循环

names = ['Micheal','Bob','Tracy']
for name in names:
    print(name)

sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
print(sum)


sum = 0
for x in range(101):
    sum = sum + x
print(sum)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n-2
print(sum)


L = ['Bart', 'Lisa', 'Adam']
for l in L:
    print('Hello,',l)

n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)


s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

i = [1,2]

t = set(i)
print(t)


s = {
    'iven': 100,
    'kven': 97,
    'linus': 89,
    'lary': 79,
    'harri': 90,
    'exit': 0xFFFFFFFF,
}
for d in s:
    print(d)
print('输入你的需要查找的姓名:')

while 1:
    name = input()
    ssd = s.get(name, False)
    if ssd == False:
        print('搜索结果:您输入的名字不存在!\n')
    else:
        x = int(s[name])
        if x == 0xFFFFFFFF:
            print('退出查询系统')
            break
        else:
            print(
                name,
                '同学你好,你的分数是:',
                x,
            )
