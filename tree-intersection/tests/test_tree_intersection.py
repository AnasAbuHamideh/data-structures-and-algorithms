from tree_intersection.tree_intersection import *
import pytest


@pytest.fixture
def creatTree1():
    bt1=Binary_search_tree()
    a_node = Node('1')
    b_node = Node('2')
    c_node = Node('3')
    d_node = Node('4')
    e_node = Node('5')
    f_node = Node('6')
    g_node = Node('7')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    b_node.right = e_node
    c_node.left = f_node
    c_node.right = g_node
    bt1.root=a_node
    return bt1

@pytest.fixture
def createTree2():
    bt2=Binary_search_tree()
    a_node = Node('8')
    b_node = Node('8')
    c_node = Node('3')
    d_node = Node('4')
    e_node = Node('5')
    f_node = Node('6')
    g_node = Node('7')
    a_node.left = b_node
    a_node.right = c_node
    b_node.left = d_node
    b_node.right = e_node
    c_node.left = f_node
    c_node.right = g_node
    bt2.root=a_node
    return bt2

def test_tree_intersection(creatTree1,createTree2):
    input=creatTree1 ,createTree2
    expexted=['3', '4', '5', '6', '7']
    actull=tree_intersection(creatTree1,createTree2)
    assert expexted==actull



def test_tree_intersection2():
    def creatTree1():
        bt1=Binary_search_tree()
        a_node = Node('1')
        b_node = Node('2')
        c_node = Node('2')
        d_node = Node('4')
        e_node = Node('5')
        f_node = Node('6')
        g_node = Node('7')
        a_node.left = b_node
        a_node.right = c_node
        b_node.left = d_node
        b_node.right = e_node
        c_node.left = f_node
        c_node.right = g_node
        bt1.root=a_node
        return bt1

    def createTree2():
        bt2=Binary_search_tree()
        a_node = Node('8')
        b_node = Node('8')
        c_node = Node('3')
        d_node = Node('4')
        e_node = Node('5')
        f_node = Node('6')
        g_node = Node('7')
        a_node.left = b_node
        a_node.right = c_node
        b_node.left = d_node
        b_node.right = e_node
        c_node.left = f_node
        c_node.right = g_node
        bt2.root=a_node
        return bt2

    bt1=creatTree1()
    bt2=createTree2()
    expexted=['4', '5', '6', '7']
    actull=tree_intersection(bt1,bt2)
    assert expexted==actull

def test_tree_intersection3():
    def creatTree1():
        bt1=Binary_search_tree()
        a_node = Node('1')
        b_node = Node('2')
        c_node = Node('3')
        d_node = Node('4')
        e_node = Node('5')
        f_node = Node('6')
        g_node = Node('7')
        a_node.left = b_node
        a_node.right = c_node
        b_node.left = d_node
        b_node.right = e_node
        c_node.left = f_node
        c_node.right = g_node
        bt1.root=a_node
        return bt1

    def createTree2():
        bt2=Binary_search_tree()
        a_node = Node('1')
        b_node = Node('2')
        c_node = Node('3')
        d_node = Node('4')
        e_node = Node('5')
        f_node = Node('6')
        g_node = Node('7')
        a_node.left = b_node
        a_node.right = c_node
        b_node.left = d_node
        b_node.right = e_node
        c_node.left = f_node
        c_node.right = g_node
        bt2.root=a_node
        return bt2

    bt1=creatTree1()
    bt2=createTree2()
    expexted=['1','2','3','4', '5', '6', '7']
    actull=tree_intersection(bt1,bt2)
    assert expexted==actull