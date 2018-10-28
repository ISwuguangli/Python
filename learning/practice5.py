# coding=UTF-8
# 数据结构
# 检查类型type
# 元组，元组不可变，有序，元素类型不单一
item = (1, 2, 'nice')

# 列表，可变，元素类型不单一
test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in test:
    print (num)

test1 = []
for i in range(1, 11):
    test1.insert(i, i)

# 使用列表解析创建列表
test2 = [i for i in range(1, 11)]

# 列表也有函数
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vec.reverse()
print (vec)

# 字典类似于哈希表
# 集合
