Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from validator_collection import checkers
... 
... def main():
...     print(is_valid(input("email: ")))
... 
... 
... def is_valid(s):
...     if checkers.is_email(s):
...         return "Valid"
...     else:
...         return "Invalid"
... 
... 
... 
... if __name__ == "__main__":