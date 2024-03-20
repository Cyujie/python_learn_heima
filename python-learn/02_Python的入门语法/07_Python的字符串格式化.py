"""
占位符类型
字符串 %s
整数 %d
浮点数 %f
"""
# 通过占位的形式,完成拼接
name = "张三"
message = "你好,我是:%s"% name
print(message)

#通过占位的形式,完成数字和字符串的拼接
name = "李四"
age = 19
message = "我的名字叫:%s,我今年%s岁"%(name,age)
print(message)

name = "望尘科技"
setup_year = 2013
stock_price = 39.99
message = "%s,成立于:%d,今天的股价是:%f"%(name,setup_year,stock_price)
print(message)

"""
如果m比数字本身宽度小,m不生效
.n会对小数部分做精度限制,同时会对小数部分做四舍五入
m,控制宽度,要求是数字
n,控制小数点精度,要求是数字
"""
num1 = 11
num2 = 11.3445
print("数字11宽度限制是5,结果是:%5d" % num1)
print("数字11宽度限制是1,结果是:%1d" % num1)
print("数字11.345宽度限制为7,小数精点2,结果是:%7.2f" % num2)
print("数字11.345宽度不限制,小数精点2,结果是:%.2f" % num2)