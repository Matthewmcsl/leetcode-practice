# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

class BSTnode:
    """
    Create a binary search tree
    """
    def __init__(self, val, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

    def getVal(self):
        return self.val
    
    def setVal(self, val):
        self.root = val

    def insert(self, val:int):
        if self.left < val:


    # def insert(self, current: Node, value: int):
    #     """
    #     Time complexity: O(logn) | We half the insertion area at every decision point
    #     """
    #     if self.root is None:
    #         self.root = Node(value)
    #     else:
    #         if value < current.value:
    #             if current.left is None:
    #                 current.left = Node(value)
    #             else:
    #                 self.insert(current.left, value)
    #         else:
    #             if current.right is None:
    #                 current.right = Node(value)
    #             else:
    #                 self.insert(current.right, value)

    def visit(self, node):
        print(node.value)

    def preorder(self, current):
        self.visit(current)
        self.preorder(current.left)
        self.preorder(current.right)


tree = BST()
n1 = Node(5)
tree.insert(None, n1)


nums = [1, 2, 3 ,4 ,5]

for i in xrange(len(nums)-2):
    