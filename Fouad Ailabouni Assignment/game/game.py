Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... while True:
...     try:
...         i = int(input("Level: "))
...         if i > 0:
...             break
...     except:
...         pass
... 
... r = random.randint(1,i)
... 
... while True:
...     try:
...         a = int(input("Guess: "))
...         if a != 0:
...             if a < r:
...                 print("Too small!")
...             elif a > r:
...                 print("Too large!")
...             else:
...                 print("Just Right!")
...                 break
...     except:
