Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l = []
... c = {}
... 
... 
... while True:
...     try:
...         a = input().upper()
...         l.append(a)
...     except EOFError:
...         print("")
...         for i in l:
...             if not i in c:
...                 c[i] = 1
...             else:
...                 c[i] += 1
... 
...         for key, value in sorted(c.items()):
...             print(value,key)
