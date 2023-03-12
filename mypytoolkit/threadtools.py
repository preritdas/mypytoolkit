"""Tools for working with threads."""
from typing import Callable, Any, List, Tuple

import queue
import threading


def list_process(operation: Callable, items: List) -> List:
    """
    Uses threading to efficiently run `operation` on `items` individually and then
    return a list of results in the same order as `items`. Best for I/O operations
    like file processing, API calls, etc.

    Args:
        operation (Callable): Must be a function that takes a single parameter, being 
            an individual element in `items`.

        items (list): A list of elements that will each be passed to `operation`.

    Returns:
        list: List of return values from calling `operation` on each item in `items`.
            The order is retained, meaning the order of elements in the returned list
            is the same order as `items` from parameters.

    Raises:
        Exception: If any operation results in an exception, the whole process will
            raise that Exception just as would happen if all operations were happening
            iteratively in the same thread.
    """
    result_queue = queue.Queue()
    exceptions: List[Exception] = []

    def store_result(text: str, index: int, result_queue: queue.Queue):
        """Runs the operation and stores the result in a queue."""
        try:
            result = operation(text)
        except Exception as e:
            exceptions.append(e)
            raise
        else:
            result_queue.put((index, result))

    threads = [
        threading.Thread(target=store_result, args=(item, index, result_queue)) 
            for index, item in enumerate(items)
    ]

    # Start the threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Check for any un-caught exceptions raised during thread execution
    if exceptions:
        raise exceptions[0]

    # Parse raw results
    raw_results: List[Luple[int, Any]] = [result_queue.get() for _ in threads]
    raw_results.sort(key=lambda tup: tup[0])  # sort by index
    return [result[1] for result in raw_results]  # discard indexes
