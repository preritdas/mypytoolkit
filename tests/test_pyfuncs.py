from mypytoolkit import pyfuncs


def test_reverse_dict():
    assert pyfuncs.reverse_dict({1: 2, '3': '4'}) == {2: 1, '4': '3'}


def test_reorder_dict():
    original = {1: 2, 3: 4, 5: 6, 7: 8}
    new_order = [3, 1, 5]

    assert pyfuncs.reorder_dict(new_order, original) == {
        3: 4,
        1: 2,
        5: 6,
        7: 8
    }
