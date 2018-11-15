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
        ####结构错误#####

# 循环
def test(self,n):
    if n<=0:
        return False
    while n%3 == 0:
        n=n//3
    return n == 1

# 递归
def test(self,n):
    if n<=0:
        return False
    if n==1:
        return True
    if n % 3 !=0:
        return False
    return self.test(n//3)
#进阶  直接判断最大值
  # maxThreeInt = 3**19
 # return n > 0 and maxThreeInt % n == 0