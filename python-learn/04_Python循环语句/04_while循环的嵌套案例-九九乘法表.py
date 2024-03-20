"""
演示使用while的嵌套循环
打印输出九九乘法表

不换行
end=""

制表符：多行字符串对齐
\t

"""

# print("一二三",end="")
# print("一二三",end="")

print("hello word")
print("java python")
print("hello\tword")
print("java\tpython")



# 定义外层的循环变量
i = 1

while i < 9:

    # 定义内层循环的控制变量
    j = 1
    while j <= i:
        # 内层循环的print语句，不要换行，通过\t制表符进行对其
        print(f"{j} * {i} = {j * i}\t",end="")
        j += 1

    i += 1
    print() # print空内容，就是输出一个换行




