Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     x = get_int()
...     print(f"{x}")
... 
... def get_int():
...     while True:
...         try:
...             a = input("a: ").split("/")
...             c = float((int(a[0]) / int(a[1]))*100)
...             if int(a[0]) <= int(a[1]):
...                 if c >= 99:
...                     print("F")
...                 elif c <= 1:
...                     print("E")
...                 else:
...                     print(f"{round(float(c))}%")
...                 exit()
...             else:
...                 return get_int()
...         except (ValueError, ZeroDivisionError):
...             continue
