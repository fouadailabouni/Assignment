Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... import tabulate
... import csv
... 
... if len(sys.argv) <= 1:
...     sys.exit("Too few command-line arguments")
... elif len(sys.argv) > 2:
...     sys.exit("Too many command-line arguments")
... elif sys.argv[1].rsplit(".")[1] != "csv":
...     sys.exit("Not a CSV file")
... 
... try:
...     with open(sys.argv[1], "r") as file:
...         reader = csv.DictReader(file)
...         print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))
... except:
