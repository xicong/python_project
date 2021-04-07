def pyWhile(): #while 循环
    i = 0
    while i<=10:
        print(i)
        i = i+1
    h = 1 #模拟一个乘法表
    while h<=9:
        l = 1
        while l<=h:
            print("%d*%d=%d"%(h,l,h*l),end=' ') # end=''可以使打印出来的*不换行
            l = l + 1
        print("") #使上面的 while 打印完可以换行
        h = h + 1