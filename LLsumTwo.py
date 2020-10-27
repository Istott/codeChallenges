
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def __init__(self, node1=None, node2=None):
    #     self.head1 = node1
    #     self.head2 = node2


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        values1 = []
        values2 = []

        while l1 is not None:
            values1.insert(0, l1.val)
            l1 = l1.next
        
        while l2 is not None:
            values2.insert(0, l2.val)
            l2 = l2.next
        
        str1 = [str(x) for x in values1]
        str2 = [str(x) for x in values2]

        res1 = int(''.join(str1))
        res2 = int(''.join(str2))

        sumtotal = res1 + res2

        sumtotalrev = [int(d) for d in str(sumtotal)]

        result = []

        for x in sumtotalrev:
            result.insert(0, ListNode(x))


        print(result)

        return




list1 = 9
list2 = 8

listNode1 = ListNode(list1)
listNode2 = ListNode(list2)

sumTot = Solution()
sumTot.addTwoNumbers(listNode1, listNode2)