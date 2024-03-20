"""
演示：快速体验函数的开发及应用
"""

# 需求，统计字符串的长度，不使用内置函数len()
str1 = "python"
str2 = "java"
str3 = "mysql"

count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度：{count}")

count = 0
for i in str2:
    count += 1
print(f"字符串{str2}的长度：{count}")

count = 0
for i in str3:
    count += 1
print(f"字符串{str3}的长度：{count}")

# 可以使用函数，来优化这个过程
def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度：{count}")


my_len(str1)
my_len(str2)
my_len(str3)
