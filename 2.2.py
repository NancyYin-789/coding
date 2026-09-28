#二分法猜数字

import random 
import time 

#模拟思考的时间

high_number = int(input("请输入猜数字的上限:"))
answer = random.randint(1, high_number)

#从1到上限随机生成一个数字

start = 1
end = high_number
guess = 0
guess_count = 0

#定义初始值，可以进入循环

while guess != answer:
    guess = (start + end ) // 2
    guess_count += 1
    print(f"我猜是：{guess},共猜了{guess_count}次")

    #每次循环都让它汇报出进行了多少次

    time.sleep(0.5)

    if guess < answer:
        print("太小了")
        start = guess + 1
    elif guess > answer:
        print("太大了")
        end = guess - 1

print(f"恭喜你，猜对啦！总共猜了{guess_count}次")
    
    