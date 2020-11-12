# Linked List
# Summary:
"""
Node class -
    value : String, Int, Object class
    next : pointer -- handle for another node
LinkedList class -
    __init__ :
    head : pointer -- handle for a node
    add()
    remove()
"""
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    totalLinkedLists = 0
    def __init__(self, node=None):
        self.head = node

    def add(self, value):
        # package the value into a Node
        newNode = Node(value)
        currentNode = self.head
        # navigate to the insertion point in the linked list
        if currentNode == None or currentNode.value > newNode.value:
            # attach newNode as the new head
            newNode.next = currentNode
            self.head = newNode
            return

        while currentNode.next.value < newNode.value:
            currentNode = currentNode.next
            if currentNode.next.next == None:
                #attach newNode as the new tail
                currentNode.next.next = newNode
                return

        # attach the node I received into this function to the end of the linked list
        newNode.next = currentNode.next
        currentNode.next = newNode

    def addToTail(self, value):
        newNode = Node(value)
        cur = self.head

        if cur is None:
            cur.value = newNode.value
            cur = cur.next

        while cur is not None:
            cur.value = newNode.value
            cur = cur.next

        # print(self.head.value)
        return self.head


    def remove(self):
        pass

"""
138 -> 156 -> 178  -> 188 -> 1333 -> 18273 -> 18383 -> None
"""
# add(50)
# newNode = node of value 50000
# currentNode = node of value 1333
# while currentNode.value < newNode.value
# currentNode = currentNode.next

arg = 23
newNode1 = Node(arg)

myList = LinkedList(newNode1)
# myList.add(newNode1)
myList.addToTail(arg)
# myList.remove(arg)

# myList2 = LinkedList(newNode1)

LinkedList.totalLinkedLists += 1

