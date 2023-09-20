Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
... 
... def main():
...     print(count(input("Text: ")))
... 
... def count(s):
...     text = re.findall(r"\b([U-u]m)\b", s)
...     return len(text)
... 
... if __name__ == "__main__":
