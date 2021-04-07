import os

if __name__ == '__main__':
    # desk = os.path.join(os.path.expanduser("~"), 'Desktop') + '\\' #mac桌面路径
    # root 当前正在访问的文件夹路径
    # dirs 该文件夹下面的子目录名 list
    # files 表示改文件夹下的文件 list
    for root,dirs,files in os.walk("/"):
        #遍历文件
        for f in files:
            path = os.path.join(root,f)
            if os.path.exists(path):
                if not os.path.getsize(path):
                    try:
                        os.remove(path)
                    except PermissionError:
                        print("PermissionError：%s" % path)
        #遍历文件夹
        for d in dirs:
            path = os.path.join(root,d)
            if os.path.exists(path):
                if not os.path.getsize(path):
                    try:
                        os.remove(path)
                    except PermissionError:
                        print("PermissionError：%s" % path)