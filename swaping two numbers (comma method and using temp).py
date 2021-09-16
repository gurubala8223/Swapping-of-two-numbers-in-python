Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Swap two number in python
>>> a=100
>>> b=200
>>> a,b=b,a
>>> print("value of a :",a)
value of a : 200
>>> print("value of b :",b)
value of b : 100
>>> #Swap two numbers by using "temp"
>>> a=100
>>> b=200
>>> temp=a
>>> a=b
>>> b=temp
>>> print('value of a:",a)
      
SyntaxError: EOL while scanning string literal
>>> print("value of a:",a)
value of a: 200
>>> print("value of b:",b)
value of b: 100
>>> 