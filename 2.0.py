#生成倒序9x9乘法表

for i in range (9, 0, -1):  #i为倒序的形式

    for j in range (1, i+1):  #j为正序的形式

        print(f"{i} * {j} = {i * j}", end="\t")  #每运行完一次乘法后都空四格

    print()  #每运行完一次循坏后换行

