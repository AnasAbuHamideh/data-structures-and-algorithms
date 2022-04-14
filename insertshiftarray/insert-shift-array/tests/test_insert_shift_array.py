from insert_shift_array.insert import insertShiftArray 

def test_case_1():
    arr = [2,4,6,-8]
    actual = insertShiftArray(arr,5)
    expected = [2,4,5,6,-8]
    assert actual == expected 

def test_case_2():
    arr = [42,8,15,23,42]
    actual = insertShiftArray(arr,16)
    expected = [42,8,16,15,23,42]
    assert actual == expected 