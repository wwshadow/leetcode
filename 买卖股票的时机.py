def maxProfit():
    # write your code here
    # 并非最大
    # result = 0
    prices=[7, 1, 5, 3, 6, 4,10]
    # for i in range(len(prices) - 1):
    #     for j in range(i + 1, len(prices)):
    #         # max() 方法返回给定参数的最大值，参数可以为序列。
    #         result = max(result, prices[j] - prices[i])
    #         print(i,result,prices[j],prices[i])
    # # return result
    # print(result)
    ############222222222222222222222222222222#####################
    # if not prices:  # 为空时返回0
    #     return 0
    # maxProfit = 0  # 最大值至少为0
    # minPurchase = prices[0]  # 初始化最小购买值
    # for price in prices:
    #     maxProfit = max(maxProfit, price - minPurchase)  # 最大利润为当前值
    # 与最小购买值之差和maxProfit的比较
    #     minPurchase = min(price, minPurchase)  # 最小购买值为当前值与minPur
    # chase之间的比较
    # # return maxProfit
    # print(maxProfit)
if __name__=="__main__":
    maxProfit()