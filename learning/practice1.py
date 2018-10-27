# coding=UTF-8
# 从键盘读取用户输入的值
# 函数返回用户输入的字符串，输出时可对字符串进行指定返回

# 输入为数值
data = input("input a data")
print(data)

# 输入为字符串
sentence = raw_input("input a str")
print ("str{0}".format(sentence))
print ("capitalize()首字母大写{0}".format(sentence.capitalize()))
print ("stripe()删除不需要的空白".format(sentence.split()))
