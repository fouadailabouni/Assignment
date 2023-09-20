Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...     dollars = dollars_to_float(input("How much was the meal? "))
...     percent = percent_to_float(input("What percentage would you like to tip? "))
...     tip = dollars * percent
...     print(f"Leave ${tip:.2f}")
... 
... 
... def dollars_to_float(dollars):
...         #TODO
...         return float(dollars.strip("$"))
... 
... def percent_to_float(percent):
...         # TODO
...         return float(percent.strip("%")) / 100
... 
