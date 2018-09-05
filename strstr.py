# if needle not in haystack:
#     return -1
# return haystack.find(needle)
#当needle 为空  返回0

def strStr():
    """
        :type haystack: str
        :type needle: str
        :rtype: int
    """
    needle = ''#//"ll"
    haystack = 'hello'
    if needle not in haystack:
        return -1
    print(haystack.find(needle))
    return haystack.find(needle)
if __name__ == __name__:
    strStr()


# 大神做法：同时解决了str 为空得问题
# # try:
# #     index = haystack.index(needle)
# #     return index
# # except:
# #     return -1
# # 描述
# # Python index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定
# 范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
# #
# # 语法
# # index()方法语法：
# #
# # str.index(str, beg=0, end=len(string))
# # 参数
# # str -- 指定检索的字符串
# # beg -- 开始索引，默认为0。
# # end -- 结束索引，默认为字符串的长度。
# # 返回值
# # 如果包含子字符串返回开始的索引值，否则抛出异常。