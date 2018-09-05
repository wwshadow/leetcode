
#python 并集union, 交集intersection, 差集difference
su = []
for i in nums1:
    if i in nums2:
        su.append(i)
return su


##大佬神迹
##利用collections.Counter的&运算，一步到位，找到 最小次数 的相同元素。
return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())