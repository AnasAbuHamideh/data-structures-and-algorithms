class Node:

    def __init__(self,value):
       self.value = value
       self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, node):
        if node == None:
            return 'Node is Empty'
        else:
            node.next = self.head
            self.head = node

        
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

    
    def zipLists(list1, list2):
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        recursive = LinkedList.zip_lists(list1.next,list2.next)

        result = list1  
        list1.next = list2  
        list2.next = recursive  

        return result
    
