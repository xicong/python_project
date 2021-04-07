def a(): #无参函数
    print("无参函数")

def a(str): #带参函数
    print(str)

def sum(a,b): # 带返回值的函数
    """
     求两个数的和
    :param a: 数据 1
    :param b: 数据 2
    :return: 和
    """
    # return a+b
    # return (a,b)  #通过元组实现返回多个数据
    return [a,b]  #通过元组实现返回多个数据


# def pyParameter(str):  # str未知参数  str,age=18缺省参数，缺省参数一定要放在未知参数后面
# def pyParameter(str, age=18):  # 如果不传会输入 age 的默认值 18
# def pyParameter(str, age=18,*args): # *args不定长参数  如果缺省参数在不定长参数后面时候，多出来的参数并不会赋值给缺省参数，会全部强行赋值给不定长参数的元组中
def pyParameter(str, age=18, *args,**kwargs): # **kwargs关键字参数 以键值对形式保存 必须放在最后面
    print(str)
    print(age)
    print(args)
    print(kwargs)

pyParameter("SS",111,222,333,444,555,666,a="xi",b=20)