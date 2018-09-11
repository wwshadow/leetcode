def merge():
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    # nums1 =sorted(nums1[:m] + nums2[0:n])
    nums3 = nums1[:m] + nums2[0:n]
    nums4 = nums1[:m] + nums2[:n]
    print(nums3,nums4)
    nums1[m:m+n] = nums2[:n]
    nums1.sort()
    print(nums1)
if __name__ == "__main__":
    merge()

    # 有两个问题： nums2[0:n] nums2[:n]  结果不同   又一样了。。。。。
    #             sorted(),sort()
#     注：
#
# sorted()与list.sort()的不同
# 　　1）list.sort() 方法返回none，sorted()返回结果
# 　　2）list.sort() 方法只可以供列表使用，而 sorted() 函数可以接受任意可迭代对象（iterable）