# coding=UTF-8
# python布尔值==,i=,not,and,or,有优先级

# python中必须严格控制代码缩进量，缩进量一致的为一个代码模块
# if语句
term = raw_input('input term')
if term == 'term':
    print ("equal")
else:
    print ("not equal")
# if else语句if elif
# 三目表达式：reply = 'true' if true else 'false'

# break与continue同c
# python循环:for，初始值，终止值，步长
for i in range(10, 1, -1):
    print (i)
print (i)
# while循环
j = 0
while j < 3:
    print(j)
    j += 1
# 计算阶乘
n = input('enter an integer')
sum1 = 1
for i in range(2,n+1):
    sum1 = sum1*i
print (sum1)
