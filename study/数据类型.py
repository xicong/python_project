def pyDataType(): #数据类型

    data1 = 0  # int
    print(type(data1))

    data2 = "Helloworld"  # 字符串
    # print(type(data2)) #字符串的类型
    # print(len(data2)) #字符串的长度
    # print(data2[0]) #通过下标获取字符
    # print(data2[0:3]) #截取 0 到 3 的字符
    # print(data2[:3])  #不写默认为 0 截取 0 到 3 的字符
    # print(data2[3:])  # 不写默认为最后 截取 3 到 最后 的字符
    # print(data2[0:10:2]) #:2为步长，选取间隔，整数从左往右，下面写法也应该是从左往右
    # print(data2[10:0:-2])  #:-2为步长，选取间隔，整数从右往左，下面写法也应该是从右往左
    # print(data2) #字符串的输出
    # data2 = input('请输入字符串：') #字符串的输入
    # print('输入的字符串为：%s'%data2)
    # print(data2.find("o")) #从左往右查找字符的位置，如果查到则返回位置，没查到则返回-1 如果有两个字符则从左往右发现第一个会后会马上返回位置
    # print(data2.find("o",0,3)) #限制查找范围 0 到 3
    # print(data2.index("o")) #和上面的 find 方法基本一致，只是这个查找的数据如果不存在会报异常
    # print(data2.index("o", 0, 6))  # 限制查找范围 0 到 3
    # print(data2.count("o")) #查询字符出现的次数
    # print(data2.replace("o","0")) #替换字符
    # print(data2.replace("o", "0",1))#1限制字符串替换次数
    # print(data2.split("o")) #将字符串分割
    # print(data2.split())  # 用空格分割

    data3 = [1, 2, 3]  # 数组  有序的对象集合
    # print(type(data3))
    # print(data3[1]) #获取列表的数据
    # data3[1] = "小何" #列表的修改
    # data3.append("小真") #直接在列表的后面添加数据
    # data3_1 = ["喜洋洋","灰太狼"]
    # data3.append(data3_1) #会直接把要添加的列表等数据当一个数据去添加进去
    # print(data3[3][0]) #列表嵌套的获取  [1, 2, 3,["喜洋洋","灰太狼"]]
    # data3.extend(data3_1) #会把数组元素拆分一个一个添加进去
    # data3.insert(0,"xi大大") #将数据添加到指定位置
    # del data3[2] #删除数据 2 位下标，实际删除的是第三个数据
    # data3.remove(2) #删除数据 2 为第二个数据
    # data3.pop() #默认删除列表的最后一个数据
    # data3.sort() #根据数据大小进行排序
    # data3.reverse() #对数据逆序
    # for pos in data3: #遍历列表
    #     print(pos)

    data4 = {"name": "字典","loc":"深圳"}  # 字典  无序的对象集合  字典可以作为 list 的元素存储
    # print(type(data4))
    # print(data4.get("name1")) #获取不存在的 key 会返回None但是不会报错
    # print(data4.get("name1","没获取到要显示的默认值"))  #可以设置获取不到后显示默认数值
    # print(data4["name"]) #获取字典的数据 获取不存在的数据会报错
    # data4["id"] = 1 #增加数据
    # data4["name"] = "字典修改"  #修改元素
    # del data4["name"] #删除元素
    # data4.clear() #清空字典数据
    # del data4 # 删除字典。删除完成后再打印会报错，因为已经不存在了
    # print(data4.keys()) #返回所有的 key
    # print(data4.values())  # 返回所有的 values
    # print(data4.items()) #返回字典数据的 k v 的数组
    # for k in data4.keys():
    #     print(k)
    # for v in data4.values():
    #     print(v)
    # for item in data4.items():
    #     print(item)
    # for k,v in data4.items():
    #     print("%s--%s"%(k,v))
    print(data4)

    data5 = (1, 2, 3)  # 元组 不能赋值相当于只读列表
    # print(type(data5))
    # for item in data5:
    #     print(item)