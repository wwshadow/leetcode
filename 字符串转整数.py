import re
def myAtoi(self):
    s = 'asd123 123 123asad'
    #正则匹配 直接匹配开始得“-+”并且保证连续得一个或多个数字，遇到其他字符结束，strip()去空格
    str1=re.findall(r'^[-+]?\d+',s.strip())
    if not str1:
        return 0
    else:
        num = int(''.join(str1))
        if num > 2**31-1:
            return 2**31-1
        elif num < -2**31:
            return -2**31
        else:
            return num
if __name__ == '__main__':
    myAtoi(1)
