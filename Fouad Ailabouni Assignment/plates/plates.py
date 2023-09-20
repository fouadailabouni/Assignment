Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     plate = input("Plate: ")
...     if is_valid(plate):
...         print("Valid")
...     else:
...         print("Invalid")
... 
... def is_valid(s):
...     if len(s) <= 6 and len(s) >= 2 and s[0:2].isalpha() and s.isalnum():
...         for i in s:
...             if i.isdigit():
...                 result = s.index(i)
...                 if s[result:].isdigit() and int(i) != 0:
...                     return True
...                 else:
...                     return False
...         return True
... 
