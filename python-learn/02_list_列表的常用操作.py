"""
演示数据日期之：list列表常用操作
"""
mylist = ['123','456','789']
# 1.1 查找某元素内的下标索引
index = mylist.index('123')
print(f'123在列表中的下标索引值是{index}')
# 1.2如果被查找的元素不存在，会报错
index = mylist.index('hello')
print(f'123在列表中的下标索引值是{index}')