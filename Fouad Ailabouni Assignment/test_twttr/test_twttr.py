Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from twttr import shorten
... 
... def main():
...     test_twttr()
... 
... def test_twttr():
...     assert shorten("word") == "wrd"
...     assert shorten("WORD") == "WRD"
...     assert shorten("WorD") == "WrD"
...     assert shorten("1234") == "1234"
...     assert shorten(".!?,") == ".!?,"
... 
... if __name__ == "__main__":
