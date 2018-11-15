def reverseBits(n):

    num=32-len(bin(n)[2:])
    m = bin(n)[2:][::-1]
    if num > 0:
        for i in range(num):
            m=m+'0'
    print(m,int(m,2))

    return m
##前几做法
        # nums=bin(n)
        # nums=nums.lstrip('0b')
        # nums=nums.zfill(32)   一直没找到。。。。原来是这个
        # nums=nums[::-1]
        # return int(nums,2)
# #2018.9.21 第一的做法
#         binNum = bin(n)
#         binStr = str(binNum)
#         binStr = binStr[2:]
#
#         reverseStr = binStr.rjust(32, '0')##。。。。。。
#         reverseStr = reverseStr[::-1]
#
#         reverseNum = int(reverseStr, 2)
#         return reverseNum
if __name__ == "__main__":
     reverseBits(43261596)