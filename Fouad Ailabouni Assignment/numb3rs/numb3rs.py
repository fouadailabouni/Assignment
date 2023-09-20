Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
... 
... def main():
...     print(validate(input("IPv4 Address: ")))
... 
... def validate(ip):
...     if numbers := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
...         for i in range(1,5):
...             if int(numbers.group(i)) > 255 or int(numbers.group(i)) < 0 :
...                 return False
...         return True
...     else:
...         return False
... 
... 
... if __name__ == "__main__":
