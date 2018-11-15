class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #转换为数学问题
        #序列 且缺失一个数
        #实际序列之和减去序列之和
        lens=len(nums)
        res=int(lens*(lens+1)//2)-sum(nums)
        return res