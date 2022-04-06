from max_stack.maxstack import Stack

def test_case_1():
   stack = Stack()
   stack.push(1)
   stack.push(2)
   stack.push(3)
   max = stack.getmax()
   actual = max
   expected = 3
   assert actual == expected

def test_case_2():
   stack = Stack()
   stack.push(10)
   stack.push(25)
   stack.push(13)
   max = stack.getmax()
   actual = max
   expected = 25
   assert actual == expected

def test_case_3():
   stack = Stack()
   stack.push(78)
   stack.push(45)
   stack.push(23)
   max = stack.getmax()
   actual = max
   expected = 78
   assert actual == expected

def test_case_4():
   stack = Stack()
   stack.push(215)
   stack.push(532)
   stack.push(230)
   max = stack.getmax()
   actual = max
   expected = 532
   assert actual == expected
   
