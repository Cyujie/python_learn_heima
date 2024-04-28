"""
样式在行数使用的时候,定义的变量作用域
"""

# # 样式局部变量
# def test_a():
#     num = 100
#     print(num)
#
#
# test_a()
# # 出了函数体,局部变量就无法使用了
# # print(num)
#
# # 样式全局变量
# num = 100
#
# def test_a():
#
#     print(f"tset_a:{num}")
#
# def test_b():
#     print(f"tset_b:{num}")
#
#
# test_a()
# test_b()
# print(num)
# # 在函数内修改全局变量
# num = 200
#
# def test_a():
#
#     print(f"tset_a:{num}")
#
# def test_b():
#     num = 500      # 局部变量
#     print(f"tset_b:{num}")
#
#
# test_a()
# test_b()
# print(num)
# global关键字,在函数内声明变量为全局变量
num = 200

def test_a():

    print(f"tset_a:{num}")

def test_b():
    global num
    num = 500      # 局部变量
    print(f"tset_b:{num}")


test_a()
test_b()
print(num)