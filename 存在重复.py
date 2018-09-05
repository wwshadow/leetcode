#1、统计数组中每个元素的个数，个数大于1，代表有重复元素。用到了collections模块
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic =collections.Counter(nums)
        for value in dic.values():
            if value>= 2:
                return True
        return False
    #2、数组变集合，检查变成集合后的长度，与原数组长度进行对比。
    class Solution(object):
        def containsDuplicate(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            if len(set(nums)) == len(nums):
                return False
            else:
                return True