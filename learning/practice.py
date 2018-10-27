# coding=UTF-8
# python入门

# python乘方运算**，求余%，整除//
# python输入和输出_字符串插入format%values
# 导入模块
import math
x = 3**2
print ('乘方运算3**2 = %.0f' % x)
# 转换说明符s:字符串 d:整数 f:浮点数
print ('字符串%s' % x)
# 格式字符串‘’.format
print ('格式字符串{0}'.format(x))
print ('格式化{y:.3f}'.format(y=3*3))
print ('z={z:.{d}f}'.format(z=1*2, d=4))
# 还可以使用模板包

# python整数长度不限，浮点数长度限制17位

# 导入模块两种模式：（1）import math
# （2）from math import*(不安全，自己的同名函数会被math模块覆盖)
# 导入指定模块 from math import sqrt,ceil等
# 导入模块类似C语言的头文件导入
print (math.ceil(x))

# 字符串长度len(),拼接+

# 类型转换
# python类型转换，float(n):将n转换为float类型，n可为字符串或整数
# 圆整round（），将小数部分为0.5圆整为最接近的偶数，
print('圆整8.5={0}'.format(round(8.5)))
print ('圆整9.5={0}'.format(round(9.5)))

# python 多行赋值
s, t = 1, 'wu'

