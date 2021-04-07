# 即在设计类时，刻意地将一些属性和方法隐藏在类的内部，这样在使用此类时，将无法直接以“类对象.属性名”（或者“类对象.方法名(参数)”）的形式调用这些属性（或方法），而只能用未隐藏的类方法间接操作这些隐藏的属性和方法。
class CLanguage:
    def setname(self, name):
        if len(name) < 3:
            raise ValueError('名称长度必须大于3！')
        self.__name = name

    def getname(self):
        return self.__name

    # 为 name 配置 setter 和 getter 方法
    name = property(getname, setname)

    def setadd(self, add):
        if add.startswith("http://"):
            self.__add = add
        else:
            raise ValueError('地址必须以 http:// 开头')

    def getadd(self):
        return self.__add

    # 为 add 配置 setter 和 getter 方法
    add = property(getadd, setadd)

    # 定义个私有方法
    def __display(self):
        print(self.__name, self.__add)


clang = CLanguage()
clang.name = "C语言中文网"
clang.add = "http://c.biancheng.net"
print(clang.name)
print(clang.add)