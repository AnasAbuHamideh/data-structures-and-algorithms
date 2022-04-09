class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """
    push will add a new Node to the stack

    input: value
    output: None
    
    """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """
    input: none
    doing: pop the top node from the stack 
    output: popped node's value
    """

        if self.is_empty():
            raise Exception("Stack is empty !")

        temp = self.top
        self.top = self.top.next
        temp.next = None

        return temp.value

    def is_empty(self):
        """
    input: None
    doing: Check if the top is none or not
    output: return a boolean
    """
        if self.top is None:
            return True
        return False


class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        

    def pre_order(self):
        """
    Input: None
    doing: traverse a tree
    output: print values of the nodes of the tree in order (root ==> left ==> right)
    """
        arr = []
        def _walk(node):
            
            arr.append(node.value)

            if node.left:
                _walk(node.left)
            if node.right:
                _walk(node.right)

        _walk(self.root)
        return arr

    def pre_order_iteration(self):
        """
    A method to traverse the tree elements
    input: nothing
    output: print the value of each node in order (root ==> left ==> right)
    """
        arr=[]
        stack = Stack()
        current = self.root

        stack.push(current)

        while not stack.is_empty():
            current = stack.pop()
            arr.append(current.value)

            if current.right:
                stack.push(current.right)

            if current.left:
                stack.push(current.left)
        return arr
    
    def in_order(self):
     '''
    Input: None
    doing: traverse a tree
    output: print values of the nodes of the tree in order (left ==> root ==> right)
     '''
     arr = []
     
     def _walk(node):
         
         if node.left:
          _walk(node.left)

         
         arr.append(node.value)
         
         if  node.right:
             _walk(node.right)

     _walk(self.root)
     return arr


    def post_order(self):
     '''
    Input: None
    doing: traverse a tree
    output: print values of the nodes of the tree in order (left ==> right ==> root )
     '''
     arr = []
     def _walk(node):

            if node.left:
                _walk(node.left)

            if node.right:
                _walk(node.right)
            
            arr.append(node.value)
    
     _walk(self.root)
     return arr

class Binary_Search_Tree(BinaryTree):
    def __init__(self):
        self.root = None
        
    
    def add(self,value):
        node = TNode(value)
        def _walk(n):
            current = n
            
            if node.value > current.value:
                if current.right:
                    _walk(current.right)
                else:
                    current.right = node
            else:
                if node.value < current.value:
                    if current.left:
                        _walk(current.left)
                    else:
                        current.left = node 
        _walk(self.root)

        


# node1 = TNode(1)
# node2 = TNode(2)
# node3 = TNode(3)
# node4 = TNode(4)
# node1.left = node2
# node1.right = node3
# node3.right = node4

# tree = BinaryTree()
# tree.root = node1

# #tree.pre_order_itiration()
# #tree.in_order_iteration()

# bst = Binary_Search_Tree()
# bst.root = node1
# bst.add(5)
# tree.pre_order_iteration()