from mypytoolkit import pyfuncs


def test_reverse_dict():
    assert pyfuncs.reverse_dict({1: 2, '3': '4'}) == {2: 1, '4': '3'}
