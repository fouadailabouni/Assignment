Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
... import csv
... 
... students = []
... 
... if len(sys.argv) < 3:
...     sys.exit("Too few command-line arguments")
... elif len(sys.argv) > 3:
...     sys.exit("Too many command-line arguments")
... elif len(sys.argv) == 3:
...     try:
...         with open(sys.argv[1], "r") as rfile, open(sys.argv[2], "w") as wfile:
...             reader = csv.DictReader(rfile)
...             for row in reader:
...                 splited = row["name"].split(",")
...                 students.append({
...                     "first": splited[1].lstrip(),
...                     "last": splited[0],
...                     "house": row["house"
...                     ]})
...             writer = csv.DictWriter(wfile, fieldnames=["first", "last", "house"])
...             writer.writerow({
...                 "first": "first",
...                 "last": "last",
...                 "house": "house"
...             })
...             for row in students:
...                 writer.writerow({
...                     "first": row["first"],
...                     "last": row["last"],
...                     "house": row["house"]
...                 })
... 
...     except FileNotFoundError:
