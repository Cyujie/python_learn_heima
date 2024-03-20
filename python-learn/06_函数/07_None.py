"""
演示特殊字面量
"""

# 无return语句的函数返回值
def say_hi():
    print("你好呀")
result = say_hi()
print(f"无返回值返回的函数，返回的内容是{result}")
print(f"无返回值返回的函数，返回的内容类型是{type(result)}")

# 主动返回None的函数
def say_hi2():
    print("你好呀")
    return None

result = say_hi2()
print(f"无返回值返回的函数，返回的内容是{result}")
print(f"无返回值返回的函数，返回的内容类型是{type(result)}")