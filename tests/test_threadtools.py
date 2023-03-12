"""Test threading tools."""
from mypytoolkit import threadtools


def test_list_process():
    def dummy_operation(integer: int) -> int:
        """Dummp op - adds 1 to an int."""
        return integer + 1

    results = threadtools.list_process(operation=dummy_operation, items=[1, 3, 5, 7, 9])
    
    # Redundant but good for checking exactly what went wrong
    assert isinstance(results, list)
    assert all(isinstance(result, int) for result in results)
    assert len(results) == 5
    assert results == [2, 4, 6, 8, 10]
