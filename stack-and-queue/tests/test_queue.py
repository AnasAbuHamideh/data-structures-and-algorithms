from stack_and_queue.queue import Queue

def test_enqueue():
  queue=Queue()
  queue.enqueue("1")
  queue.enqueue("2")
  queue.enqueue("3")
  actual = queue.rear.value
  expected = "3"
  assert actual == expected
  
def test_dequeue():
    queue = Queue()
    queue.enqueue("1")
    queue.enqueue("2")
    queue.enqueue("3")
    queue.dequeue()
    actual = queue.front.value
    expected = "2"
    assert actual == expected

def test_is_empty_queue():
    queue = Queue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_peek_of_queue():
  queue=Queue()
  queue.enqueue("1")
  queue.enqueue("2")
  queue.enqueue("3")
  actual = queue.peek()
  expected = "1"
  assert actual == expected

