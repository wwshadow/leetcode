def hammingWeight(n):
    """
    :type n: int
    :rtype: int
    """
    n=bin(n)
    count = 0
    for i in n:
        if i ==str(1):
            count+=1
    print(count)
if __name__ == "__main__":
    hammingWeight(0)