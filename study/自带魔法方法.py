class Cat:

    #属性
    def __init__(self,new_name,new_age): #初始化 每次创建的时候执行
        print("---------init--------------")
        self.name = new_name
        self.age = new_age

    def __str__(self): #打印方法内返回的字符串内容
        return "%s今年%s了"%(self.name,self.age)

    def __del__(self): #当对象掉用完成时候会掉用 del 方法删除创建的对象
        print("---------del--------------")

    #方法
    def introduce(self):
        print("%s今年%s了"%(self.name,self.age))


cat = Cat("小红",20)
# cat.introduce()
print(cat)  #如果没有 str 方法打印出来的是这个对象在电脑内的对象内存地址 如果有则打印出 str 内返回的字符串内容