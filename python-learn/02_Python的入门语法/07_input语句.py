"""
演示Python的input语句
获取键盘的输入信息
"""
print("请告诉我你是谁?")
name = input()
print("我知道了,你是:%s"% name)

name = input("请告诉我你是谁")
print(f"我知道了,你是:{name}")

# 输入数字类型
num = input("请告诉我你的银行卡密码:")
# 数据类型转换
num = int(num)
print("你的银行卡密码类型是:",type(num))

user_name = input("请输入您的用户名")
user_type = input("您是尊贵的:ssssvip用户")
print("欢迎您的光临")