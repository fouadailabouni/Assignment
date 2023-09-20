Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def main():
...         time = input("What time is it? ")
...         meal = convert(time)
...         if meal >= 7 and meal <=8:
...                 print("breakfast time")
...         elif meal >= 12 and meal <=13:
...                 print("lunch time")
...         elif meal >= 18 and meal <= 19:
...                 print("dinner time")
... 
... def convert(time):
...         hour, min = time.split(":")
...         hour = float(hour) + (float(min) / 60)
...         return hour
... 
... if __name__ == "__main__":
