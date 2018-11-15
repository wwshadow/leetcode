
def fizzBuzz():
    """
    :type n: int
    :rtype: List[str]
    """
    n=1
    lists=[]
    for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            lists.append('FizzBuzz')
        elif i%3 == 0:
            lists.append('Fizz')
        elif i%5 == 0:
            lists.append('Buzz')
        else:
            lists.append(str(i))
            # format 格式化
    print(lists)

if __name__ == "__main__":
    fizzBuzz()