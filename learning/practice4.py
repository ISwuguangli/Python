# coding=UTF-8
# python字符串可直接通过索引访问，索引有正索引和负索引
"""
    三引号用于生成说明文档
"""
s = 'nice'
print (s[len(s)-1])
print (s[-1])
# python 字符串遍历，类似c的foreach,java的增强for循环
for c in s:
    print(c)
# 转义字符\,计算字符串长度时会忽略

# s[begin:end]返回begin到end-1
print(s[1:3])

# python提供了字符串检测、搜索、改变大小写、设置格式、剥除函数、替换、注意r函数名从右开始扫描
# python中也可使用正则表达式