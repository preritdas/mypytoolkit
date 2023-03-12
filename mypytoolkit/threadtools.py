"""Tools for working with threads."""
from typing import Callable


def list_process(operation: Callable, items: list) -> list:
    """
    Uses threading to efficiently generate a list of dashed summaries instead of 
    generating them sequentially.

    The `operation` must be an operation that takes a single string parameter and
    returns a single string. This was built to bulk process window summaries and window
    title generation.
    """
    result_queue = queue.Queue()
    exceptions: list[Exception] = []

    @tools.exponential_backoff(
        retries=5, 
        base_delay=1, 
        exceptions=(openai.OpenAIError,), 
        exception_string_match="rate limit"
    )
    def store_result(text: str, index: int, result_queue: queue.Queue):
        """Summarizes the text and adds it to the queue."""
        try:
            result = operation(text)
        except Exception as e:
            exceptions.append(e)
            raise
        else:
            result_queue.put((index, result))

    threads = [
        threading.Thread(target=store_result, args=(text, index, result_queue)) 
            for index, text in enumerate(texts)
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
    raw_results: list[tuple[int, str]] = [result_queue.get() for _ in threads]
    raw_results.sort(key=lambda tup: tup[0])  # sort by index
    return [result[1] for result in raw_results]  # discard indexes
