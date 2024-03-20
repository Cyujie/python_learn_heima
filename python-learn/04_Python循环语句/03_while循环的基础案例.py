"""
演示while循环的基础案例 - 猜数字
"""

# 获取范围在1-100的随机数字
import random
num = random.randint(1,10)

# 通过一个布尔类型的变量，做循环是否继续的标记
chishu = 0
flag = True
while flag:
    guess_num =  int(input("请输入你猜测的数字："))
    chishu += 1
    if guess_num == num:
        print("恭喜你猜对了")
        flag = False
    else:
        if guess_num >num:
            print("你猜的数字太大了")
        else:
            print("你猜的数字太小了")

print(f"你猜测的次数为{chishu}")
