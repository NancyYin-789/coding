money = float(input("请输入充值金额："))
new = input("请输入您是否为新顾客，是或否；")

gift = 0
subsidy = 0
first_gift = 0
new_or_old = 0

#上面四行的目的是：最后输出的时候不会报错。

if money >= 10000:
    gift = 10000
    total = money + gift

elif money >= 5000:
    gift = money * 0.2
    subsidy = 500
    total = money + gift + subsidy

elif money >= 3000:
    gift = money * 0.18 
    total = money + gift

elif money >= 1500:
    gift = money * 0.15
    total = money + gift

else : total = money

if new == "是":
    first_gift = gift * 0.1 
    total += first_gift

if new == "是":
    new_or_old = "新"

else: new_or_old = "老"

#原本这里我用了双等号，ai提醒我改成单等号

total = money + gift + subsidy + first_gift

result = f"尊敬的{new_or_old}客户您好！您充值的金额是{money}元，实际到账{total}元！"
print (result)

#最后忘记写print了...还好ai提醒我了一下！