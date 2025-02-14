"""
演示数据日期之：list列表常用操作
"""
mylist = ['123','456','789']
# 1.1 查找某元素内的下标索引
index = mylist.index('123')
print(f'123在列表中的下标索引值是{index}')
# 1.2如果被查找的元素不存在，会报错
# index = mylist.index('hello')
# print(f'123在列表中的下标索引值是{index}')


#2.修改特定下标索引的值
mylist[0] = '最佳球会'
print(f'列表被修改元素值后,结果是：{mylist}')

#3.在指定下标位置插入新元素
mylist.insert(1,'bset')
print(f'列表插入元素后，结果是{mylist}')

#4.在列表的尾部追加‘‘‘单个’’’新元素
mylist.append('deepseek')
print(f'列表追加元素后，结果是{mylist}')

#5.在列表的尾部追加‘‘‘一批’’’新元素
mylist_2 = ['1','2','3']
mylist.extend(mylist_2)
print(f'列表在追加了一个新的元素后，结果是:{mylist}')