import re

# 正则表达式学习
#
# 正则表达式规则

# match 匹配正则方法   在字符串中从头查询匹配的字符
# search 匹配正则方法   在字符串中搜索查询需要的字符不需要一一对应去查找
# fandall  找出所有的
# sub  根据规则替换对应的字符
# compile

# 单字符匹配
# .   匹配任意一个字符（除了\n）
# []  匹配[]中列举的字符
# \d  匹配数字，0-9
# \D  匹配非数字，不是数字的字符
# \s  匹配空白，空格内容
# \S  匹配非空白
# \w  匹配单词字符 a-z A-Z 0-9 _
# \W  匹配非单词字符

# 多字符匹配

# *      匹配前一个字符出现 0 次或者无限次 即可有可无
# +      匹配前一个字符出现 1 次或者无限次 即至少一次
# ？     匹配前一个字符出现 0 次或者出现一次 即要么是一次要么是 0 次
# {m}    匹配一个字符出现 m 次
# {m,n}  匹配一个字符出现从 m 次到 n 次

# 匹配开头和结尾

# ^      匹配字符串开头  
# $      匹配字符串结尾

# ()     单独规划区域做匹配   并且里面的值可以通过 group(1)表示取出第一个括号里面的内容

# r      re.match(r"\d\\","3\8") r可以不用转换特殊字符

# |             匹配左右一个任意一个表达式
# (ab)          将括号中的字符作为一个分组
# \num          引用分组 num 匹配到的字符串
# (?p<name>)    分组起别名
# (?P=name)     引用别名为 name 分组匹配到的字符串



# res = re.match('hello1','hello world')
# print(res)
# print(res.group())  #若正则匹配到则返回数据 若没有匹配到返回none  若匹配到数据的话用group来提取

# .
# res = re.match('h...o','hello world')  #一个.对应一个字符，一一对应
# print(res.group())

# []
# res = re.match('[Hh]','hello world')  #可以同时匹配大小写字符,即大写的 H 也可以正常匹配出，小写的h也可以匹配出
# print(res.group())
# res= re.match('[Hh]','Hello world')
# print(res.group())
# res = re.match('[0-9]','1993838world') #匹配任意数字
# print(res.group())
# res = re.match('[a-z]','world') #匹配任意小写字母
# print(res.group())
# res = re.match('[A-Z]','World') #匹配任意大写字母
# print(res.group())

# \d \D
# res = re.match('[\d]','1world') #匹配任意数字
# print(res.group())
# res = re.match('[\D]','_world') #匹配任意非数字
# print(res.group())

# \s \S
# res = re.match('w\so','w orld')  #匹配空格
# print(res.group())
# res = re.match('w\Sr','world')  #匹配非空格
# print(res.group())

# \w \W
# res = re.match('\w\w\w\w','0aA_')  #匹配单词字符 a-z A-Z 0-9 _
# print(res.group())
# res = re.match('\W\W\W\W','@#￥%')  #匹配非单词字符
# print(res.group())

# 多字符匹配练习

# * 匹配的字符 0 次或者无限次
# res = re.match('发射\d*次','发射123456789次')  #匹配所有数字
# print(res.group())
# res = re.match('.*','发射123456789次')  #匹配所有字符
# print(res.group())

# +  匹配的字符至少一次
# res = re.match('\d+','123456789')
# print(res.group())

# ? 匹配出现 0 次或者 1 次
# res = re.match('\d?','')
# print(res.group())

# {m}  匹配出现 m 次
# res = re.match("\d{3}","111")
# print(res.group())

# {m,n} 从 m次到 n 次
# res = re.match("\d{10,20}","0123456789")
# res = re.match("\d{2}","0123456789")
# print(res.group())

#实例应用

# res = re.match("[A-Z][a-z]*","MnnM")
# print(res.group())
# res = re.match("[A-Z][a-z]*","Mnnnhhhggggg")
# print(res.group())

# names = ["name1","_name","2_name","_name_"]
# for name in names:
#     res = re.match("[a-zA-Z_][\w]*",name)
#     if res:
#         print("变量名 %s 有效",res.group())
#     else:
#         print("变量名 %s 无效",name)

# res = re.match("[1-9]?[0-9]","117")  #十位数可有可无 ？
# print(res.group())

#密码匹配 8到 20 位  可以是大写字母小写字母数字下划线
# res = re.match("[a-zA-Z0-9_]{8,20}","WJSSSssss0097")
# print(res.group())
# res = re.match("\w{8,20}","WJSSSssss0097")
# print(res.group())

# 匹配163邮箱 且@符号之前有 4 到 20 位
# res = re.match(".{4,20}@163.com","hello@163.comssssssddddd")
# print(res.group())

# email_list = ["hello@163.com","hello@163.comsssssss","hello@qq.com"]
# for email in email_list:
#     res = re.match(".{4,20}@163\.com$",email)    #加\.才能表示原来的. 不然则表示规则的任意字符
#     if res:
#         print(res.group())
#     else:
#         print(res)

# res = re.match("[a-zA-Z]\w{3,19}@163\.com$|@126\.com$|@qq\.com$","hello@163.com")
# print(res.group())

# res = re.match("[a-zA-Z]\w{3,19}@(163|126|qq)\.com$","hello@163.com")
# print(res.group())
# print(res.group(1)) #可以通过 group(1)表示取出第一个括号里面的内容

# res = re.match("\d\\\\","3\8")     #四个反斜杠才能表示一个反斜杠
# print(res.group())

# res = re.match(r"\d\\","3\8")     #r可以不用转换特殊字符
# print(res.group())

# res = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>","<html>hh</html>")
# print(res.group())

# res = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>","<html>hh</htmlffffff>")   # 还能正常打印 这是不对的，前端标签必须对称 看下面
# print(res.group())
# res = re.match(r"<[a-zA-Z]{4}>\w*</[a-zA-Z]{4}>","<html>hh</htmlffffff>")     #进一步限制长度 4 个 进一步解决看下面
# print(res.group())
# res = re.match(r"<([a-zA-Z]{4})>\w*</\1>","<html>hh</html>")         #\num 处理匹配前端标签  用（）括起来前面的内容 后面用/1 表示第一个小括号的内容
# print(res.group())
# res = re.match(r"<(\w*)><(\w*)>.*</\2></\1>","<html><h1>www.baidu.com</h1></html>")
# print(res.group())

# 匹配分组  （?P<起的名字>规则）
# res = re.match(r"<(?P<html>\w*)><(?P<h1>\w*)>.*</(?P=h1)></(?P=html)>","<html><h1>www.baidu.com</h1></html>")
# print(res.group())
# print(res.group("html"))
# print(res.group("h1"))

#search
# res = re.match(r"\d+","阅读次数是 9999 还是 9998？")     # 直接报错，从开始查询没有
# print(res.group())
# res = re.search(r"\d+","阅读次数是 9999 还是 9998？")      # 会查询到第一个并打印出来 怎么打印出所有匹配的字符 看下面
# print(res.group())

# fandall 找出所有的
# res = re.findall(r"\d+","阅读次数是 9999 还是 9998？")
# print(res)
# res = re.findall(r"\d+","阅读次数是  还是 ？")     # 若没有数字则返回[]
# print(res)

# sub  根据规则替换对应的字符
# res = re.sub(r"\d+","998","123 python = 97",1)    #根据规则替换对应的字符，默认替换掉所有的，第四个参数表示只替换几个
# print(res)
# def add(temp):         # sub 掉用函数处理
#     strNum = temp.group()
#     num = int(strNum)+1
#     return str(num)
# res = re.sub(r"\d+",add,"python = 0")
# print(res)

#sub  实例应用
# test_str = """
# <dd class=job-advantage>
#     <span class=" advantage>职位诱感:</span>
#     <p>带年假、六险一金、年餐补助、平管理</p>
# </dd>
# <p>热悉Linux操作系统:</p>
# <p>熟悉HTTP、TCP/IP等协议:</p>
# <p>熟悉常用数据结构及算法:</p>
# <p>精通 Python,掌爬虫技术,熟悉scrp框架、 spider架等:</p>
# <p>熟悉分布式、缓存、消息等机制,例如: redis、 Act ivem、 kafka、 mongodb;</p>
# <p>熟悉全少一种Sa1数据(myq1/ postgresql/ solserver/ oracle/dtb2):</p>
# <p>有卡富的反爬虫:</p>
# <p>优秀的分析、解決题能力,对处理未知的、挑战性问充满激情:</p>
# <p>熟悉高井发、高性能的分布式系统的设计及应用,熟悉常用数据存储,各种数据处理技术优先:</p>
# """
# res = re.sub(r"<[^>]*>","",test_str)  #^放在中括号中会起到取反的作用
# print(res)

# compile
# text = "Hello, I am Panghu, from Nanjin, nice to meet you..."
# regex = re.compile("\w*h\w*",re.I)  # re.I 忽略大小写  re.M 多行匹配，会影响^$  re.S 会让.匹配包含换行符在内的所有字符
# print(regex)
# res = regex.findall(text)
# print(res)