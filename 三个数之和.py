def threeSum(k):
    lists=[-1, 0, 1, 2, -1, -4]
    lists.sort(reverse=True)
    print(lists)
    for index,i in enumerate(lists):
        for x in range(0,(len(lists))):
            j = index + x
            if j >= len(lists):
                continue
            for m in range(0,len(lists)):
            # print(x,index,i)

                n = index+m
                if n>len(lists) or j == n or index == n or j==index:
                    continue
                else:
                    print("编号",index,j,n)
                    a=lists[index]
                    b=lists[j]
                    c=lists[n]
                    # print("数值",a,b,c)
                    if a==b+c:
                        print(i,j,n)
if __name__=="__main__":
    threeSum(0)