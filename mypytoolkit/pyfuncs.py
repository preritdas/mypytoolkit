def tprint(arg):
    """Prints the contents of a variable/object along with its type."""
    print(arg, type(arg))

def count(iterable, value):
    """Returns an integer of the number of occurences of a value in an iterable."""
    count = 0
    for item in iterable:
        if item == value:
            count += 1
    return int(count)

def reverse_dict(dic: dict):
    """Reverses the keys and values in a dictionary."""
    new_dict = {}
    for key, val in dic.items():
        new_dict[val] = key
    return new_dict