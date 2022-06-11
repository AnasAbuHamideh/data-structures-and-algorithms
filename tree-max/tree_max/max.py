class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self):
        self.root = None

    def pre_order(self):
       arr=[]
       def _walk(node):
           arr.append(node.value)

           if node.left:
               _walk(node.left)

           if node.right:
                _walk(node.right)
       _walk(self.root)
       return arr

    def maximum(self):
        arr = self.pre_order()
        max = self.root.value
        for i in arr:
            if i > max:
                max = i
        return max
        