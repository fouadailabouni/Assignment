Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cash = 50
... 
... while cash > 0:
...         print(f"Amount due: {cash}")
...         cent = int(input("Amount Due:"))
...         if cent == 10 or cent == 25 or cent == 5:
...                 cash -= cent
... 
