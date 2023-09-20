Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from datetime import date
... import inflect
... import sys
... 
... p = inflect.engine()
... 
... 
... def main():
...         birthday = input("Date: ")
...         return diff(birthday)
... 
... def diff(birthday):
...     try:
...         year, month, day = birthday.split("-")
...         birthday = date(int(year), int(month), int(day))
...     except:
...         return sys.exit("Invalid")
...     difference =  (date.today() - birthday).days * 24 * 60
...     result = p.number_to_words(difference, andword="").capitalize()
...     print(result + " minutes")
...     return result + " minutes"
... 
... 
... if __name__ == "__main__":
