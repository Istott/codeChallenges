#given a binary search tree, write a function kth smallest to find the kth smallest element in it.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def addElement(self, node):
        if node.val < self.val:
            if self.left == None:
                self.left = node
            else:
                self.left.addElement(node)

        if node.val > self.val:
            if self.right == None:
                self.right = node
            else:
                self.right.addElement(node)

class Solution(object):
    def kthSmallest(self, root, k):
        self.count = 1
        self.foundK = None
        
        def inOrder(node):
            if not node or self.foundK:
                return
            
            inOrder(node.left)

            if self.count == k:
                self.foundK = node.val
            self.count += 1
            inOrder(node.right)

        inOrder(root)

        print(self.foundK)
        return self.foundK


            #traverse down to the smallest node value, counting its way through.
            #count my way up to kth node and return node value

        
target = 14
rootnode = TreeNode(30)
arr = [2,3,5,6,7,89,9,1,14,23,234,45,13,77,33,55]

for x in arr:
    rootnode.addElement(TreeNode(x))

smallest = Solution()
smallest.kthSmallest(rootnode, target)