"""
演示判断语句的实战案例：猜数字
"""
# 1.构建一个随机的数字变量
import random
num = random.randint(1,10)
# print(f"随机生成的数字为：{num}")

gress_num = int(input("请输入猜想的数字："))

# 通过if判断生语句进行数字的猜测
if gress_num == num:
    print("恭喜第一次猜想就对了")
else:
    if gress_num > num:
        print("你猜测的数字太大了，再试一试")
    else:
        print("你猜测的数字太小了再试一试")

    gress_num = int(input("请再输入猜想的数字："))

    if gress_num == num:
        print("恭喜第二次猜对啦")
    else:
        if gress_num > num:
            print("你猜测的数字太大了，再试一试")
        else:
            print("你猜测的数字太小了再试一试")







