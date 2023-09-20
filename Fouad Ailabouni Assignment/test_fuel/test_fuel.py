Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from fuel import convert, gauge
... import pytest
... 
... def main():
...     test_convert()
...     test_gauge()
... 
... def test_convert():
...     assert convert("1/4") == 25
...     assert convert("2/4") == 50
...     assert convert("3/4") == 75
...     assert convert("1/100") == 1
...     assert convert("99/100") == 99
...     with pytest.raises(ValueError):
...         convert("one/zero")
...     with pytest.raises(ZeroDivisionError):
...         convert("1/0")
... 
... def test_gauge():
...     assert gauge(50) == "50%"
...     assert gauge(1) == "E"
...     assert gauge(100) == "F"
...     assert gauge(99) == "F"
... 
... if __name__ == "__main__":
