
for i in nums:

    if nums.count(i) == 1:

        return i
    ##下面的v2.0版本是为了缩减代码，但效率上没有任何改善。

        for i in nums:
            if nums.count(i) == 1:
                return i
    #看了别人的代码，发现我第一个版本的思路还不错，只是将列表s换成字典会好很多。

        s = {}
        for i in nums:
            if i in s.keys():
                s.pop(i)
            else:
                s[i]=1
        return list(s.keys())[0]

    ##异或操作 0异或任何数不变，任何数与自己异或为0
    res = 0
        for i in nums:
            res^=i
        return res

    ##最神奇
    return sum(list(set(nums)))*2-sum(nums)