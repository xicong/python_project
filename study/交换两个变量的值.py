def pyVariableInterchange(): #交换两个变量的值
    a = 8
    b = 10

    #第一种方法
    # c = a
    # a = b
    # b = c

    #第二种方法
    # c = [a,b]
    # a = c[1]
    # b = c[0]

    #第三种
    a,b = b,a  #py 中独有的方法

    print(a)
    print(b)

pyVariableInterchange()