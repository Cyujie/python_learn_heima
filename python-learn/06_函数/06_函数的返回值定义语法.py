"""
演示：定义函数返回值的语法格式
"""

# 定义一个函数，完成2数相加功能
def add(a,b):
    results = a + b
    # 通过返回值，将相加的结果返回给调用者
    return results
    # 返回结果够，还想输出一句话
    print("我完事了")


# 函数的返回值，可以通过变量去接收
r = add(1,2)
print(r) 