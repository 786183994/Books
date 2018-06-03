# _*_ coding: utf-8 _*_
__auther__ = '刘凌晨'
__date__ = '2018/5/20 10:55'

from random import Random


#生成随机字符串
def readom_str(random_length=8):
    str = ""
    #表示随机生成的字符串必须在这些里面进行选取
    chars = '0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0,length)]
    return str


def book_certificates():
    """
        藏书正编号
    :return:
    """
    src = "C326" + readom_str(8)
    return src
