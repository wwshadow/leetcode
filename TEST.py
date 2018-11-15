# class Solution:
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(set(nums)) == len(nums):
#             return False
#         else:
#             return True
#
#
# def stringToIntegerList(input):
#     return json.loads(input)


def test(n):
    # import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')
    #
    # lines = readlines()
    # while True:
    #     try:
    #         line = next(lines)
    #         nums = stringToIntegerList(line);
    #
    #         ret = Solution().containsDuplicate(nums)
    #
    #         out = (ret);
    #         print(out)
    #     except StopIteration:
    #         break
    # if n < 3:
    #     print("false")
    #     return False
    # while True:
    #     m = n % 3
    #     n = n / 3
    #     if n == 1:
    #         print("true")
    #         return True
    #     elif m!=0:
    #         print("FA")
    #         return False
    #     elif n != 1 and m ==0:
    #         test(n)

test(27)
