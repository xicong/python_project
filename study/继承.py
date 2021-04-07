# 面向对象  封装 继承 多态

class D:

    def __init__(self):
        self.num1 = 1000

    def d_print_num(self):
        print(self.num1+10)

#父
class A:

     def __init__(self):
         self.num = 10

     def print_num(self):
         print(self.num+10)

#子
class B(A): #继承

    # pass #如果子类啥都没写写这个
    def print_num1(self):
        print(self.num+20)


class C(B,D): #再继承  多继承



    # def print_num(self):  #方法重写 丢弃父函数的所有东西
    #     print(self.num + 100)

    def print_num(self):  #方法重写 保留父类所有东西，再增加新的东西
        super().print_num()  #
        print(self.num + 100)

    def print_num2(self):
        print(self.num + 30)


# b = B()
# b.print_num()
# b.print_num1()
# c = C()
# c.print_num()
# c.print_num1()
# c.print_num2()
# c.d_print_num()