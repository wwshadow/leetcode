
#filter()
# filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。
# 该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回
#  True 的元素放到新列表中。

#isalnum  如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False

s = list(filter(str.isalnum, s.lower()))
return True if s == s[::-1] else False