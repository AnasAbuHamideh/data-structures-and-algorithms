class Node :
  def __init__(self,value):
    self.value=value
    self.next=None


class Queue :
  def __init__(self):
    self.front=None
    self.rear=None

  def enqueue(self,value):
    node = Node(value)

    if not self.front :
      self.rear = node 
      self.front = node 
      
    else:  
      self.rear.next = node 
      self.rear = node 
      
  def dequeue(self) :
    temp = self.front
    self.front = self.front.next
    temp.next = None

  def is_empty(self):
    return self.front == None 

  def peek(self):
    return self.front.value
