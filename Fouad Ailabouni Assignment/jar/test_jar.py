Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from jar import Jar
... 
... def test_init():
...     jar = Jar()
...     assert jar.capacity == 12
...     jar1 = Jar(1)
...     assert jar1.capacity == 1
... 
... def test_str():
...     jar = Jar()
...     assert str(jar) == ""
...     jar.deposit(1)
...     assert str(jar) == "🍪"
...     jar.deposit(11)
...     assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
... 
... 
... def test_deposit():
...     jar = Jar()
...     jar.deposit(5)
...     assert jar.size == 5
...     jar.deposit(5)
...     assert jar.size == 10
... 
... 
... def test_withdraw():
...     jar = Jar()
...     jar.deposit(10)
...     jar.withdraw(5)
...     assert jar.size == 5
...     jar.withdraw(5)
