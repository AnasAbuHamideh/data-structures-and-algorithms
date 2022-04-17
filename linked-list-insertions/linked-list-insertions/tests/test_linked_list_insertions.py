from linked_list_insertions.insertion import LinkedList,Node


def test_append_to_the_end():
    ll = LinkedList()
    node1 = Node('A')
    node2 = Node('B')
    ll.insert(node1)
    ll.append(node2)
    actual = ll.head.next.value
    expected = 'B'
    assert actual == expected


def test_add_multiple_nodes_to_the_end():
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    ll.append(node1)
    ll.append(node2)
    actual = ll.head.value
    expected = 1
    assert actual == expected
    assert ll.head.next.value == 2


def test_insert_before_node_located_middle():
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    ll.append(node1)
    ll.append(node2)
    ll.insert_before(2, 4)
    actual = ll.head.next.value
    expected = 4
    assert actual == expected


def test_insert_before_first_node_in_linked_list():
    ll = LinkedList()
    node1 = Node(1)
    ll.append(node1)
    ll.insert_before(1, 0)
    actual = ll.head.value
    expected = 0
    assert actual == expected
    


def test_insert_after_node_in_the_middle():
    ll = LinkedList()
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    ll.append(node1)
    ll.append(node2)
    ll.append(node3)
    ll.insert_after(2, 1.5)
    actual = ll.head.next.next.value
    expected = 1.5
    assert actual == expected


def test_insert_after_last_in_the_linked_list():
    ll = LinkedList()
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    ll.append(node1)
    ll.append(node2)
    ll.append(node3)
    ll.insert_after("C", "D")
    actual = ll.head.next.next.next.value 
    expected = 'D'
    assert actual == expected