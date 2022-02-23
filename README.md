# My Python Toolkit

This is just a miscellaneous collection of some tools I use regularly that I decided to compile into one package for easy use by mainly me. All examples will assume the package has been imported as `kit`. 

Install from PyPi: `pip install mypytoolkit`. 

```python
import mypytoolkit as kit
```

## Dates and Times

`kit.time_now()` returns a string of the current time in the format "%H-%M". Midnight is "00-00" and 8:35 a.m. is "08-35". 10 p.m. is "22-00". 

`kit.today_date()` returns a string of the current date in the format "%Y-%M-%D", where Feb 22, 2022, is "2022-02-22". 

## Python Tools

`kit.tprint()` displays the contents of an object along with its type. I got fed up of constantly writing `print(obj, type(obj))` when debugging so I found myself constantly defining a `tprint()` function:

```python
def tprint(obj):
    print(obj, type(obj))
    return [obj, type(obj)]
```

Super simple but it makes a night and day difference when debugging in lightspeed.

## Document Checks

`kit.are_docs_same()` will tell you if two documents (of any type) have the _exact_ same contents. It takes two parameters. 

```python
kit.are_docs_same(original_dir: str, new_dir: str)
```

It returns a boolean, `True` or `False`, depending on whether the contents of the two files are identical. There is no grey area.