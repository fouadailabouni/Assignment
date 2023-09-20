Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... 
... if len(sys.argv) <= 1:
...     sys.exit("Too few command-line arguments")
... elif len(sys.argv) >= 3:
...     sys.exit("Too many command-line arguments")
... elif sys.argv[1].rsplit(".")[1] != "py":
...     sys.exit("Not a Python file")
... try:
...     with open(sys.argv[1], "r") as file:
...         count = 0
...         for line in file:
...             if not line.lstrip().startswith("#") and line.lstrip() != "":
...                 count += 1
...     print(count)
... 
... except:
