Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     text = input("Input: ")
...     shorten(text)
... 
... def shorten(word):
...     #text = input("Input: ")
...     l = ["a", "A", "E", "e", "I", "i", "O", "o", "U", "u"]
...     out = ""
... 
...     for i in word:
...             if not i in l[:]:
...                     out += i
...     return out
... 
... if __name__ == "__main__":
