from stack_queue_pseudo.pseudo_queue import PesudoQueue

def test_enqueue():
    queue = PesudoQueue()
    queue.enqueue("1")
    queue.enqueue("2")
    actual = "2"
    expected = queue.front.value
    assert  actual == expected

def test_dequeue():
    queue=PesudoQueue()
    queue.enqueue('1')
    queue.enqueue("2")
    actual= '2'
    expected=queue.dequeue()
    assert  actual == expected


