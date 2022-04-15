from linked_list.linked_list import Node,LinkedList

def test_Linked_List():
    li = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    li.insert(node1)
    li.insert(node2)
    actual = li.head.value
    expected = 1
    assert actual == expected

def test_Linked_List_insert():
    li = LinkedList()
    node1 = Node("A")
    node2 = Node("B")
    li.insert(node1)
    li.insert(node2)
    actual = li.head.value
    expected = "A"
    assert actual == expected

def test_Linked_List_includes():
    li = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    li.insert(node1)
    li.insert(node2)
    actual = li.includes(1)
    expected = True
    assert actual == expected

def test_Linked_List_toString():
    li = LinkedList()
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    li.insert(node1)
    li.insert(node2)
    li.insert(node3)
    actual = li.toString()
    expected = "[A] -->[B] -->[C] -->None"
    assert actual == expected