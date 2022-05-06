import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [1,2,3,4,5,6,7,8,9,0]
    test_arr = [0,1,2,3,4,5,6,7,8,9]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [1,2,3,4,5,6,7,8,9,0]
    test_arr = [9,8,7,6,5,4,3,2,1,0]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [1,2,3,4,5,6,7,8,9,0]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_moreten():
    result = []
    input_arr = [1,2,3,4,5,6,7,8,9,0,1]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 1)

def test_bubble_sort_lessten():
    result = []
    input_arr = [1,2,3,4,5,6,7,8,9]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 2)

def test_bubble_sort_zero():
    result = []
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 0)

def test_bubble_sort_nonint():
    result = []
    input_arr = [1,2,3,4,5,6,7,8,9,0.5]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 3)