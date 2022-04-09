from trees.tree import TNode,BinaryTree,Binary_Search_Tree

def test_pre_order():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = tree.pre_order()
    expected = [1,2,3,4] 
    assert actual == expected
    
def test_pre_order_iteration():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = tree.pre_order_iteration()
    expected = [1,2,3,4]
    assert actual == expected

def test_in_order():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = tree.in_order()
    expected = [2,1,3,4]
    assert actual == expected

def test_post_order():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    tree = BinaryTree()
    tree.root = node1
    actual = tree.post_order()
    expected = [2,4,3,1]
    assert actual == expected

def test_binary_search_tree():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    #tree = BinaryTree()
    #tree.root = node1
    bst = Binary_Search_Tree()
    bst.root = node1
    bst.add(5)
    actual = bst.pre_order()
    expected = [1,2,3,4,5]
    assert actual == expected

def test_binary_search_tree2():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    #tree = BinaryTree()
    #tree.root = node1
    bst = Binary_Search_Tree()
    bst.root = node1
    bst.add(5)
    actual = bst.pre_order_iteration()
    expected = [1,2,3,4,5]
    assert actual == expected

def test_binary_search_tree3():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    #tree = BinaryTree()
    #tree.root = node1
    bst = Binary_Search_Tree()
    bst.root = node1
    bst.add(5)
    actual = bst.post_order()
    expected = [2,5,4,3,1]
    assert actual == expected

def test_binary_search_tree4():
    node1 = TNode(1)
    node2 = TNode(2)
    node3 = TNode(3)
    node4 = TNode(4)
    node1.left = node2
    node1.right = node3
    node3.right = node4
    #tree = BinaryTree()
    #tree.root = node1
    bst = Binary_Search_Tree()
    bst.root = node1
    bst.add(5)
    actual = bst.in_order()
    expected = [2,1,3,4,5]
    assert actual == expected
