def hammingDistance( x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    count=0
    a=x^y
    for i in bin(a):
        if i == '1':
            count+=1
    print(count)
if __name__ == "__main__":
    hammingDistance(1,4)
