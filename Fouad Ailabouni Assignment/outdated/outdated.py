Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l = [
...     "January",
...     "February",
...     "March",
...     "April",
...     "May",
...     "June",
...     "July",
...     "August",
...     "September",
...     "October",
...     "November",
...     "December"
... ]
... 
... while True:
...     date = input("Date: ")
...     try:
...         if "/" in date:
...             month, day, year = date.split("/")
...             if int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31:
...                 break
... 
...         elif "," in date:
...                 date = date.replace(",", "")
...                 month,day,year = date.split(" ")
...                 if month in l and int(day) <= 31:
...                     month = l.index(month) + 1
...                     break
...     except:
...         print()
...         pass
... 
... 
