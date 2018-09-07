def removeNthFromEnd():
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    head=[1, 2, 3, 4, 5]
    n=2
    lists = []
    num = 0
    while (head):
        lists.append(head)
        head = head.next
        num += 1
    if num == 0:
        return None
    if lists[-n].next == None:
        lists[-n - 1].next = None
        return None
    else:
        lists[-n].val = lists[-n].next.val
        lists[-n].next = lists[-n].next.next
    return lists[0]
if __name__ == '__main__':
    removeNthFromEnd()