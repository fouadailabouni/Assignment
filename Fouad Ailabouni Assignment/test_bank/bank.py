Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     a = input("Greeting: ")
...     value(a)
... 
... def value(a):
...     b = a.lower().strip()
... 
...     if not b.find("hello"):
...         return 0
... 
...     elif b[0] == "h":
...         return 20
... 
...     else:
...         return 100
... 
... if __name__ == "__main__":
