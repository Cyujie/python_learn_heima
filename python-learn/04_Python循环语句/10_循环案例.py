"""
演示循环综合案例：发工资
"""
# # 定义账户余额
# money = 10000
# # for循环对员工发放工资
# for i in range(1,21):
#     import random
#     score = random.randint(1, 10)
#
#     if score < 5:
#         print(f"{i}号员工绩效分{score},不满足，不发工资，下一位")
#         # continue跳过发放
#         continue
#
#     #  要判断余额足不足
#     if money >= 1000:
#         money -= 1000
#         print(f"{i}号员工发工资1000元，公司账户余额剩余{money}元")
#     else:
#         print(f"公司账户余额不够发放，当前余额{money}，下个月在发")
#         # break结束发放
#         break


import random

def distribute_salary(money, employee_count):
    for i in range(1, employee_count + 1):
        score = random.randint(1, 10)

        if score < 5:
            print(f"{i}号员工绩效分{score},不满足，不发工资，下一位")
            continue

        if money >= 1000:
            money -= 1000
            print(f"{i}号员工发工资1000元，公司账户余额剩余{money}元")
        else:
            print(f"公司账户余额不够发放，当前余额{money}，下个月在发")
            break

    return money

# 定义账户余额
money = 10000000
# 员工数量
employee_count = 200

# 调用函数进行工资发放
remaining_money = distribute_salary(money, employee_count)

