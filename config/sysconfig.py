# -*- coding: utf-8 -*-

# 截图路保存径，绝对路径，也可以用相对路径
SCREENSHOTURL = '../sreenshot/'

# 时间样式
ISOTIMEFORMAT = '%Y%m%d%H%M%S'



def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    # path = path.strip()
    # # 去除尾部 \ 符号
    # # path = path.rstrip("\\")
    # path = path.strip("*")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    for p in path:
        if p in " ?.!/;:*|":
            path2=path.replace(p, '')
    isExists = os.path.exists(path2)
    # 判断结果
    if not isExists:
        os.makedirs(path2)
        print(path2 + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path2 + ' 目录已存在')
        return False


# import re
# string = "12345464我不是药神123456abcdefgABCVDFF？/ ，。,.:;:''';'''[]{}()（）《》*|"
# print(string)
#
# sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",string)
# print(sub_str)
