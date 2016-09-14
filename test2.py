Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: C:\Users\KLUBnyaKprO\My documents\GitHub\test_python\test.py ===
need buy one bread
>>> range(10)
range(0, 10)
>>> range(6, 10)
range(6, 10)
>>> range (7, 16, 2)
range(7, 16, 2)
>>> _
range(7, 16, 2)
>>> 
>>> 
>>> _
range(7, 16, 2)
>>> print(range(7,16,2))
range(7, 16, 2)
>>> for x in range(5):
	print("hello")

hello
hello
hello
hello
hello
>>> _
range(7, 16, 2)
>>> for x in range(5):
	print("hello" + x)

Traceback (most recent call last):
  File "<pyshell#13>", line 2, in <module>
    print("hello" + x)
TypeError: Can't convert 'int' object to str implicitly
>>> for x in range(5):
	print("hello", x)

hello 0
hello 1
hello 2
hello 3
hello 4
>>> m = [1, 3, 5, 7, 9]
>>> m
[1, 3, 5, 7, 9]
>>> m[1]
3
>>> m[-1]
9
>>> a = []
>>> a
[]
>>> a.ap
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a.ap
AttributeError: 'list' object has no attribute 'ap'
>>> a.append (3)
>>> a
[3]
>>> a = a + [2]
>>> a
[3, 2]
>>> a += [7]
>>> a
[3, 2, 7]
>>> b = [8, 9]
>>> a += b
>>> a
[3, 2, 7, 8, 9]
>>> p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> p
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> p[1:7]
[1, 2, 3, 4, 5, 6]
>>> p[-3:]
[7, 8, 9]
>>> p[0:9:2]
[0, 2, 4, 6, 8]
>>> p[7:0:-1]
[7, 6, 5, 4, 3, 2, 1]
>>> family = ["mother", "dad", "sister", "bro"]
>>> family
['mother', 'dad', 'sister', 'bro']
>>> "sister" in family
True
>>> "dog" in family
False
>>> numbers = [3, 1, 19, 85, 2]
>>> numbers
[3, 1, 19, 85, 2]
>>> len(numbers)
5
>>> len(family )
4
>>> max(numbers)
85
>>> min(numbers)
1
>>> list("Alex")
['A', 'l', 'e', 'x']
>>> numbers[3] = 44
>>> numbers
[3, 1, 19, 44, 2]
>>> del numbers [2]
>>> numbers
[3, 1, 44, 2]
>>> 
