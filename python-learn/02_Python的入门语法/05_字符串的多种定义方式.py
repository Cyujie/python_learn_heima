"""
演示字符串的三种定义方式：
- 单引号定义法
- 双引号定义法
- 三引号定义法
"""

# 单引号定义
name = '张三'
print(type(name))
# 双引号定义
name = "张三"
print(type(name))
# 三引号定义
name = """李四,张三"""
print(type(name))

# 在字符串内,包含双引号
name = '"你好python"'
print(name)
# 在字符串内包含单引号
name = "'你好python'"
print(name)
# 在转义字符 \ 解除引号的效用
name = "\"你好python\""
print(name)
name = '\'你好python\''
print(name)