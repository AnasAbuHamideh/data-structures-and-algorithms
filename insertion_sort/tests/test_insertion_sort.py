from insertion_sort.inserton import insertion_Sorts


def test_insertion_1():
    arr = [8,4,23,42,16,15]
    expected = [4,8,15,16,23,42]
    actual = insertion_Sorts(arr)
    assert actual == expected

def test_insertion_2():
    arr = [20,18,12,8,5,-2]
    expected = [-2, 5, 8, 12, 18, 20]
    actual = insertion_Sorts(arr)
    assert actual == expected
    

def test_insertion_3():
    arr = [5,12,7,5,5,7]
    expected = [5, 5, 5, 7, 7, 12]
    actual = insertion_Sorts(arr)
    assert actual == expected
    

def test_insertion_4():
    arr = [2,3,5,7,13,11]
    expected = [2, 3, 5, 7, 11, 13]
    actual = insertion_Sorts(arr)
    assert actual == expected
    