## 实际 寻找算法  最快找出某个数

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #二分法

        mins,maxx=0,n
        while(True):
            mid =(mins+maxx)/2
            if isBadVersion(mid)==False and isBadVersion（mid+1）== True:
                return mid+1
            elif isBadVersion(mid)==False and isBadVersion（mid+1）== False:
                mins = mid
            else isBadVersion(mid)==True and isBadVersion（mid+1）== True:
                maxx = mid

#这个更合理
# if n <= 0: return 0
# if n == 1: return 1
# l = 1
# r = n
# while l < r:
#     m = int((l + r) / 2)
#     if isBadVersion(m):
#         r = m  # 因为在这里不是m-1因此有可能变成无限循环
#     else:
#         l = m + 1
# return r
