"""
演示for循环的练习题:数一数有几个a
"""
# 统计以下数字有几个a
name = "salkfalkmardaklsdaio skla lkaadlaada3"

# 定义一个变量，用来统计有多少个a
count = 0

# 循环统计
# for 临时变量 in 被统计的数据：
for x in name:
        if x == "a":
            count += 1

print(f"字符集中有{count}个a")


