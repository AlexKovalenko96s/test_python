Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
===================== RESTART: C:\Python projects\fun.py =====================
>>> import fun
>>> fun.func(9)
88
>>> import imp
>>> imp.reload(mod_import)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    imp.reload(mod_import)
NameError: name 'mod_import' is not defined
>>> imp.reload(fun)
<module 'fun' from 'C:\\Python projects\\fun.py'>
>>> fun.func(2)
11
>>> fun.func(3)
16
>>> 
==================== RESTART: C:/Python projects/echo.py ====================
__name__ есть __main__
>>> import echo
__name__ есть echo
>>> 
=================== RESTART: C:/Python projects/echoV2.py ===================
Я основная программа
>>> import echoV2
Я другой модуль, меня импортировали
>>> 
==================== RESTART: C:/Python projects/funV2.py ====================
Введите значение:
777
603736
>>> import funV2
Введите значение:
777
603736
>>> import funV2.
SyntaxError: invalid syntax
>>> import funV2.func(2)
SyntaxError: invalid syntax
>>> 
==================== RESTART: C:/Python projects/funV2.py ====================
Введите значение:
4
23
>>> import funV2
>>> funV2.func(2)
11
>>> 

>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> 
