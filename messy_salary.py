salary='$876,001'
>>> salary=salary.replace('$','')
>>> salary=salary.replace(',','')
>>> salary=int(input("salary"))
salary
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    salary=int(input("salary"))
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> salary
'876001'
>>> 
