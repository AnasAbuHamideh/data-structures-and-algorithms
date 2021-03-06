
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

    def peek(self):
        '''function return the value of the top node'''
        return self.top.value
   

    def is_empty(self):
        '''method to check if stack is Empty return boolean'''
        return self.top == None 
