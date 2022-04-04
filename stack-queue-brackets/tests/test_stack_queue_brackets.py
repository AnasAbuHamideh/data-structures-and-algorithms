from stack_queue_brackets.brackets import validate_brackets

def test_case_1():
    value = '()'
    actual = validate_brackets(value)
    expected = True
    assert actual == expected

def test_case_2():
    value = '(){}[]'
    actual = validate_brackets(value)
    expected = True
    assert actual == expected

def test_case_3():
    value = '()[[Extra Characters]]'
    actual = validate_brackets(value)
    expected = True
    assert actual == expected

def test_case_4():
    value = '(){}[[]]'
    actual = validate_brackets(value)
    expected = True
    assert actual == expected