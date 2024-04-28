"""
演示嵌套调用函数
"""

# 定义函数func_b
def fun_b():
    print("---2---")
# 定义行数func_a,并在内部调用func_b
def func_a():
    print("---1---")

    # 调用fun_b
    fun_b()

    print("---3---")
# 调用行数func_a
func_a()