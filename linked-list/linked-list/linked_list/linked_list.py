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
    

if __name__ == "__main__" :
    li = LinkedList()
    node1 = Node("1")
    node2 = Node("2")
    li.insert(node1)
    li.insert(node2)
    print(li.includes("1"))
    print(li.toString())
    