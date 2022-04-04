class Dog:
    def __init__(self,value):
        self.value = "dog"

class Cat:
    def __init__(self,value):
        self.value = "cat"

class AnimalShelter:
    def __init__(self):
        self.front= None
        self.queue = None
    
    def enqueue(self,animal):
        if animal == "dog":
            node = Dog()
            if not self.front :
                self.rear = node 
                self.front = node 
      
            else:  
                self.rear.next = node 
                self.rear = node

        elif animal == "cat":
            node = Cat()
            if not self.front :
                self.rear = node 
                self.front = node 
      
            else:  
                self.rear.next = node 
                self.rear = node

    def dequeue(self,pref):
        while self.front != None:
            temp = self.front
            self.front = self.front.next
            if temp.value == pref:
                 temp.next = None
                 return temp.value
        return "Animal Not Exist"