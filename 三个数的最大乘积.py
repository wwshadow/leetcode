#!/usr/bin/python
# -*- coding: UTF-8 -*-
def nums():
    num = [-4,-3,-2,-1,60]
    print(type(num))
    num.sort(reverse=True)
    print(num)
    n_num=num[0]*num[1]*num[2]
    print(n_num)
if __name__=="__main__":
    nums()
