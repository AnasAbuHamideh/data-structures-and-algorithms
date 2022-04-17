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
    
    def append(self, value):
        if value == None:
            return 'Node is Empty'
        else:
            if self.head is None:
                self.head = value
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = value

    
    def insert_before(self,value,new_value):
        node = Node(new_value)
        current = self.head
        while current:
            if current.value == value:
                node.next = current
                self.head = node
                return

            if current.next:
                if current.next.value == value:
                    node.next = current.next
                    current.next = node
                    return
                current = current.next

        return f'{value} Not Found'

    def insert_after(self,value,new_value):
        node = Node(new_value)
        current = self.head
        while current:
            if current.value == value:
                node.next = current.next
                current.next = node
                return
            current = current.next
            
        return f'{value} not Found'