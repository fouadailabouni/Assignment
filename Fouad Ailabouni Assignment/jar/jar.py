Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Jar:
...     def __init__(self, capacity=12):
...         if capacity > 0:
...             self._capacity = capacity
...             self._size = 0
...         else:
...             raise ValueError("Wrong capacity")
... 
...     def __str__(self):
...         return self.size * '🍪'
... 
...     def deposit(self, n):
...         if n > self.capacity or (self.size + n) > self.capacity:
...             raise ValueError("Over capacity")
...         self._size += n
... 
...     def withdraw(self, n):
...         if n > self.size:
...             raise ValueError
...         self._size -= n
...     @property
...     def capacity(self):
...         return self._capacity
... 
...     @property
...     def size(self):
