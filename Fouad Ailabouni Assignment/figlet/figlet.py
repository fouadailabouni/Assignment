Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pyfiglet import Figlet
... import sys
... import random
... 
... figlet = Figlet()
... figlet.getFonts()
... 
... 
... if len(sys.argv) == 1:
...     isRandom = True
... elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
...     isRandom = False
... else:
...     print("Invalid Usage")
...     sys.exit(1)
... 
... if isRandom == False:
...     try:
...         figlet.setFont(font=sys.argv[2])
...     except:
...         print("Invalid usage")
...         sys.exit(1)
... else:
...     font = random.choice(figlet.getFonts())
... 
... 
... text = input("Input:")
