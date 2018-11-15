# 题目分析：
# # **设f(n)为n阶台阶的情况下，所有不同的跳法方法的总和！**
# # 1.如果起始跳一阶的话，剩余的n-1阶就有 f(n-1) 种跳法；
# # 2.如果起始跳二阶的话，剩余的n-2阶就有 f(n-2) 种跳法；
# # 所以f(n) = f(n-1) + f(n-2)，实际结果即为斐波纳契数。 fibonacci


def climbStairs():
    """
    :type n: int
    :rtype: int
    """
    n=6
    nums = [0, 1, 2]

    if n == 1:
        return nums[1]
    elif n == 2:
        return nums[2]
    else:
        for i in range(3, n + 1):

            nums.append(nums[i - 1] + nums[i - 2])
            print(i,nums)
    # return nums[n]
    print(nums[n],n)
# tmpList = [1,1]
#         for i in range(0,n-1):
#             x = tmpList[-1] + tmpList[-2]
#             tmpList.append(x)
#         return tmpList[-1]
if __name__=="__main__":
    climbStairs()


