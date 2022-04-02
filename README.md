# My Python Toolkit

This is just a miscellaneous collection of some tools I use regularly that I decided to compile into one package for easy use by mainly me. All examples will assume the package has been imported as `kit`. 

Install from PyPi: `pip install mypytoolkit`. 

```python
import mypytoolkit as kit
```

## Dates and Times

### Time Now
`kit.time_now()` returns a string of the current time in the format "%H-%M". Midnight is "00-00" and 8:35 a.m. is "08-35". 10 p.m. is "22-00". That's without optional parameters.

The optional parameter `int_times: bool` will allow the function to return a tuple instead of a string. If you call `kit.time_now(int_times = True)`, and if the time is 8:35 a.m., you will receive a tuple `(8, 35)` where each element is an integer. This is useful for performing relative time actions within a program that are hour/minute independent. 

----
`kit.today_date()` returns a string of the current date in the format "%Y-%M-%D", where Feb 22, 2022, is "2022-02-22". 

`kit.time_decimal()` returns a float of the time. For example, if it is 8:45 a.m., the function will return 8.75. 

`kit.weekly_time_decimal()` returns a float of how far you're in a week. For example, midnight on Monday is `0`, noon on Wednesday is `2.5`, and 4 p.m. on Sunday is `6.66`. 

## Python Tools

Simple Python-specific tools to make life easier, from `print` options to functions for working with iterables.

### Type Printing

`kit.tprint()` displays the contents of an object along with its type. I got fed up of constantly writing `print(obj, type(obj))` when debugging so I found myself constantly defining a `tprint()` function:

```python
def tprint(obj):
    print(obj, type(obj))
    return [obj, type(obj)]
```

Super simple but it makes a night and day difference when debugging in lightspeed.

### Iterable Counting

`kit.count()` will accept an iterable item and a value. It returns an integer of the exact number of occurrences of the value in the iterable. Many iterable objects have in-built class methods for counting values (`iterable_object.count()` for example). But many iterables returned by APIs, for example, don't, so it makes sense to have some global method for counting values. 

This way, many objects can be passed to the method, too.

## Files

Tools for working with files.

### Same Document Contents

`kit.are_docs_same()` will tell you if two documents (of any type) have the _exact_ same contents. It takes two parameters. 

```python
kit.are_docs_same(original_dir: str, new_dir: str)
```

It returns a boolean, `True` or `False`, depending on whether the contents of the two files are identical. There is no grey area.

### Appending Content to Files

`kit.append_by_query()` will append content to a file in a line below the first occurrence of a query. 

See a demonstration:

[![asciicast](https://asciinema.org/a/4lHkZOkC4kfzZMgRQs3S8wRVn.svg)](https://asciinema.org/a/4lHkZOkC4kfzZMgRQs3S8wRVn)

Here is a written example. If `test.txt` has the contents:

```
this is line 1!
line 2 is here.
hello people!
line number 4.
```

And we run:

```python
import mypytoolkit as kit

kit.append_by_query(
    query = 'hello', 
    content = 'Just added this.', 
    file_path = 'test.txt',
    insert_above = False # unnecessary, it is by default
)
```

`test.txt` is modified in place and is now:

```
this is line 1!
line 2 is here.
hello people!
Just added this.
line number 4.
```

| Parameter | Necessity | Behavior |
| --- | --- | --- |
| `query` | Required | The first occurrence of this string is where the toolkit will look to insert `content` (above or below depending on `insert_above`). |
| `content` | Required | The content inserted above or below the first occurrence of `query` in the document. |
| `file_path` | Required | A string of the path to the file the toolkit will search through and write in. | 
| `insert_above` | Optional | Boolean. By default, `insert_above = False`, and the toolkit will insert `content` the line below the first occurrence of `query`. If `True`, the toolkit will insert `content` in a line above instead. |

## Math

Added a `LinearEquation` class that takes attributes of slope and intercept on instantiation. It has a `plot()` method which plots the linear graph. For example:

```python
import mypytoolkit as kit

equation = kit.LinearEquation(slope = 4, intercept = 10)
equation.plot(interval = 1000)
```

This will output a `matplotlib` plot of the linear equation from 0 to 1000.
