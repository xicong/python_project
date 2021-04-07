def pyUnpacking(): #拆包 需要拆的数据的个数要和变量的个数相同

    # 元组
    # m = 1,2,3 #拿元素只能通过下标比较麻烦
    # a,b,c = m #拆包
    # print(a)
    # print(b)
    # print(c)

    # 列表
    # m = [1, 2, 3]  # 拿元素只能通过下标比较麻烦
    # a, b, c = m  # 拆包
    # print(a)
    # print(b)
    # print(c)

    # 字典 字典拆包，拆出来的是 key 值
    m = {"name": "字典","loc":"深圳"}  # 拿元素只能通过下标比较麻烦
    a, b = m  # 拆包
    print(a)
    print(b)

pyUnpacking()