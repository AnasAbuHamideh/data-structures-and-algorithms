class Node:

    def __init__(self,value):
       self.value = value
       self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head is None:
            self.head = node

        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

        
    def includes(self, value):
      current=self.head
      while current and current.next != None:
          if current.value == value:
              return True
          current=current.next
      return False


    def toString(self):
        output = ""
        if self.head is None:
            output = "Empty linked list"
        else:
            current = self.head
            while(current):
                output+= f'[{current.value}] -->'
                current = current.next
            
            output+= "None"
        return output

    def kthFromEnd(self,k):
        current=self.head
        if k<0:
            return 'k is negative, please enter a positive number'
        counter=0
        while current.next:
            counter +=1
            current=current.next
        if counter+1==k:
            return 'the k value is equal to the length of the list'
        if counter<k:
            return 'invalid Error'
        position=counter-k
        current=self.head
        for x in range(position):
            current=current.next
        return current.value