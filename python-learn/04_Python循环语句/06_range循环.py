"""
演示python中的range()语句的基本使用
"""

# range语法1 range（num）
# for x in range(10):
#     print(x)

# 练习题
count = 0
for x in range(1,100):
    if x % 2 == 0:
        count += 1

print(f"1-100(不包含100)有{count}个偶数")

