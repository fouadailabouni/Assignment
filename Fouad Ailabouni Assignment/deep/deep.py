Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
... 
... b = a.lower().replace("-","").replace(" ","")
... 
... if b == "fortytwo" or b == "42":
...         print("Yes")
... else:
