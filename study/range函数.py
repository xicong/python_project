def pyRange(): #创建一个整数列表，一般用for 循环中
    # range(start,stop,step) start开始下标 0  stop结束下标，不包括 stop，  step 步长 ，默认 1
    # range(0,10) #[0,1,2,3,4,5,6,7,8,9]
    # range(2,9)  # [2,3,4,5,6,7,8]
    # range(10)  # [0,1,2,3,4,5,6,7,8,9]
    # range(0,20,3)  #[0,3,6,9,12,15,18]
    # range(0,30,5)  # [0,5,10,15,20,25]
    list = [0,1,2,3,4,5,6,7,8,9]
    # for i in list:
    #     print(i)
    for i in range(len(list)):
        print(i)

pyRange()