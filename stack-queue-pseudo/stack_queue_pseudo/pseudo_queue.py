class Node:

    def __init__(self,value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self,Node = None):
        self.top = Node
        
    def push(self,value):
        '''function adds a new node with that value to the top of the stack'''
        node = Node(value)
        self.next = self.top
        self.top = node

    def pop(self) :
        '''function Removes the node from the top of the stack'''
        temp = self.top
        self.top = self.top.next
        temp.next= None

        return temp.value
        
    def is_empty(self):
        '''method to check if stack is Empty return boolean'''
        return self.top == None 

class PesudoQueue:

    def __init__(self):
        '''function creates queue with 2 stacks'''
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.front = self.stack1.top
        self.rear = self.stack2.top
    

    def enqueue(self,value):
        '''function adds node to stack1'''
        node = Node(value)
        node.next = self.front
        self.front = node
        self.stack1.push(node)

    def dequeue(self):
        '''function Removes node from queue'''
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop().value
    