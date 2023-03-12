"""Exponential backoff decorator."""
from typing import Callable, Tuple, Union
from functools import wraps

import time
import random


def exponential_backoff(
    retries: int = 5,
    base_delay: float = 1,
    exceptions: Union[BaseException, Tuple[BaseException]] = (Exception,),
    exception_string_match: str = ""
) -> Callable:
    """
    A decorator that adds exponential backoff retry logic to a function.
    Args:
        retries: The maximum number of times to retry the decorated function.
        base_delay: The base delay time (in seconds) for exponential backoff.
        exceptions: A tuple of exception types to catch and retry. Default is (Exception,).
        exception_string_match: A string that must be present in the Exception string body.
    Returns:
        A decorator that adds exponential backoff retry logic to a function.
    """
    def decorator(func: Callable) -> Callable:
        """
        The actual decorator that adds exponential backoff retry logic to a function.
        Args:
            func: The function to decorate.
        Returns:
            The decorated function with exponential backoff retry logic.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """
            The wrapper function that adds exponential backoff retry logic to a function.
            Returns:
                The return value of the decorated function.
            Raises:
                The original exception if the maximum number of retries is exceeded.
            """
            for i in range(retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    # Conditions for not retrying, thereby re-raising
                    if i == (retries - 1) or exception_string_match.lower() not in str(e).lower():
                        raise e

                    delay = base_delay * (2 ** i) + random.random()
                    print(f"Error occurred, retrying in {delay:.2f} seconds...")
                    time.sleep(delay)

        return wrapper
    return decorator
