Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = input("File name: ")
... 
... b = a.split(".")
... 
... match b[-1].lower().strip():
...         case "gif":
...                 print("image/gif")
...         case "jpg" | "jpeg":
...                 print("image/jpeg")
...         case "png":
...                 print("image/png")
...         case "pdf":
...                 print("application/pdf")
...         case "txt":
...                 print("text/plain")
...         case "zip":
...                 print("application/zip")
...         case "txt":
...                 print("text/plain")
...         case "bin" | _ :
