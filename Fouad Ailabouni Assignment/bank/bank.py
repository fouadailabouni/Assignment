Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = input("Greeting:")
... 
... b = a.lower().replace(" ","")
... 
... if not b.find("hello"):
...         print("$0")
... 
... elif b[0] == "h":
...         print("$20")
... 
... else: