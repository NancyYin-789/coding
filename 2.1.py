from time import sleep 

def progress_bar (sleep_time, function):
    """
       生成进度条函数

       参数：
       sleep_time : 停顿的时间
       function:加载完成后执行的函数

       返回：
       加载完成！
       """

    for i in range (0, 101):

        print(f"\r正在加载中:{'★' * i} {'☆' * (100-i)} {i}%", end="\r")

        #当进度条在运行的过程中，我都让它在前面显示“正在加载中”
        
        sleep(sleep_time)

        #在这个循环中，让它停顿指定的时间

    print(f"\r加载完成! {'★' * 100} ")

    #当到100的时候，不再显示“正在加载中”，而显示“加载完成！”

    return "感谢您的耐心等待！"

def finish_function():
    return "加载完成！"       


value = progress_bar(0.02 , finish_function)

#调用上面定义的finish函数

print(value)        

#定义停顿的时间为0，02秒