# coding:utf-8
def longestCommonPrefix(strs):
    if not strs:
        return ''
    if len(strs) == 1:
        return strs[0]
    mins = min([len(x) for x in strs])
    # print(minl)
    # print(strs)
    end = 0
    while end < mins:
        for i in range(1,len(strs)):
            # print(strs[i],strs[i][end],strs[i-1],strs[i-1][end])
            if strs[i][end]!= strs[i-1][end]:
                # print(strs[0][:end])
                return strs[0][:end]
        end += 1
    # print(strs[0][:end])
    return strs[0][:end]
if __name__ == "__main__":
    strs=["flower","flow","flight"]
    longestCommonPrefix(strs)
####简直是。。#####os.path.commonprefix(strs)