from linked_list_kth.llkth import LinkedList,Node

def test_kth_greater_than_the_list():
    ll = LinkedList()
    ll.insert(Node(10))
    ll.insert(Node(20))
    ll.insert(Node(30))
    ll.insert(Node(40))
    actual = ll.kthFromEnd(6)
    expected = "invalid Error"
    assert actual == expected


def test_the_linked_list_size_is_one():
    ll = LinkedList()
    ll.insert(Node(10))
    actual = ll.kthFromEnd(0)
    expected = 10
    assert actual == expected


def test_kth_is_negative_int():
    ll = LinkedList()
    ll.insert(Node(10))
    ll.insert(Node(20))
    ll.insert(Node(30))
    ll.insert(Node(40))
    actual = ll.kthFromEnd(-2)
    expected = "k is negative, please enter a positive number"
    assert actual == expected


def test_kth_and_ll_are_the_same():
    ll = LinkedList()
    ll.insert(Node(10))
    ll.insert(Node(20))
    ll.insert(Node(30))
    ll.insert(Node(40))
    actual = ll.kthFromEnd(0)
    expected = 40
    assert actual == expected