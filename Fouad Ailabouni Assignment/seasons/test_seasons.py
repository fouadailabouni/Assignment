Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pytest
... from seasons import diff
... 
... def main():
...     test()
... 
... def test():
...     assert diff("2022-01-20") == "Five hundred twenty-five thousand, six hundred minutes"
...     assert diff("2021-01-20") == "One million, fifty-one thousand, two hundred minutes"
...     with pytest.raises(SystemExit, match="Invalid"):
...         diff("Januar 6th, 1998")
... 
... 
... 
... if __name__ == "__main__":
