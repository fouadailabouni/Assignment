Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pytest
... from um import count
... 
... def main():
...     test1()
... 
... 
... 
... def test1():
...     assert count("um") == 1
...     assert count("um?") == 1
...     assert count("Um, thanks for the album") == 1
