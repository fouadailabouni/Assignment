Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from bank import value
... 
... def main():
...     test_value()
...     test_value_20()
...     test_value_100()
... 
... def test_value():
...     assert value("hello") == 0
...     assert value("hello Hi") == 0
...     assert value("HeLLo") == 0
... 
... def test_value_20():
...     assert value("hi") == 20
...     assert value("HoI") == 20
...     assert value("Hi") == 20
... 
... def test_value_100():
...     assert value("What's up") == 100
...     assert value("Good Morning") == 100
...     assert value("Welcome!") == 100
... 
... 
... if __name__ == "__main__":
