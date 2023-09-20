Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x, y, z = input("Expression: ").split(" ")
... 
... if y == "+":
...         print(float(x) + float(z))
... elif y == "-":
...         print(float(x) - float(z))
... elif y == "*":
...         print(float(x) * float(z))
... elif y == "/":
