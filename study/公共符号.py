def pyPublicSymbols(): #公共符号 + * in not in
    # + 拼接
    # print("HELLO"+"WORLD")  #HELLOWORLD
    # print([1, 2, 3]+[1, 2, 3])  #[1, 2, 3, 1, 2, 3]
    # print((1, 2, 3) + (1, 2, 3))  # (1, 2, 3, 1, 2, 3)

    # * 数据复制  字典不能用
    # print("="*10) #==========
    # print([1, 2, 3]*3) #==========
    # print((1, 2, 3) * 3) # (1, 2, 3, 1, 2, 3, 1, 2, 3)

    # in 判断是否存在变量里   not in判断不在   对字典操作时候判断的是key
    # print("A" in "ABC")  # True在
    # print(12 in [1,2,3]) # FALSE 不存在
    # print(3 in (1, 2, 3)) # True在
    # print("loc" in  {"name": "字典","loc":"深圳"})  #对字典操作时候判断的是key

    # len
    # print(len("abc")) # 字符长度
    # print(len([1, 2, 3])) #数组的长度
    # print(len((1, 2, 3))) #元组的长度
    # print(len({"name": "字典","loc":"深圳"})) #键值对的对数

    # max min
    # print(max([1, 2, 3]))
    # print(min([1, 2, 3]))
    # print(max((1, 2, 3)))
    # print(min((1, 2, 3)))
    # print(max({"a": "a=","b":"b="}))  #比较 v 的值大小返回 k
    # print(min({"a": "a=", "b": "b="}))

    #  del
    delData = [1, 2, 3]
    del delData[0]
    del delData