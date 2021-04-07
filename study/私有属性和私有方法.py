class Person:

    def __init__(self):
        #私用属性
        self.__id = "身份证号码：xxxxxx"  #加__可以使属性成为私有属性 私有属性只能在类里面操作

    def __peocess_bug(self):  #私有方法  私有方法可以被对象里面通过非私有方法掉用处理
        print("专业处理")

    def look_id(self,psw):
        if psw == 123456: #私有属性只能在类里面操作
            print(self.__id)
        else:
            print("保密")

person = Person()
person.look_id(123456)