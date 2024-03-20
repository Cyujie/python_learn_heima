"""
演示循环语句的中断控制：break和continue
continue:中断所在循环的当次执行，直接进入下一次
break:直接结束所在的循环
"""

# 演示循环中断语句 continue
# for i in range(1,6):
#     print("语句1")
#     continue
#     print("语句2")
# 演示continue的嵌套应用
# for i in range(1,6):
#     print("语句1")
#     for j in range(1,6):
#         print("语句2")
#         continue
#         print("语句3")
#     print("语句4")
# 演示循环中断语句break
# for i in range(1,6):
#     print("语句1")
#     break
#     print("语句2")
# print("语句3")
# 演示break的嵌套应用
for i in range(1,6):
    print("语句1")
    for j in range(1,6):
        print("语句2")
        break
        print("语句3")
    print("语句4")