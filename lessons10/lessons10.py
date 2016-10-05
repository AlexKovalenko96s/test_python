Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> v = {'aa', 'e', 1, '5'}
>>> v
{'e', 1, 'aa', '5'}
>>> v.add(1)
>>> v
{'e', 1, 'aa', '5'}
>>> type(v)
<class 'set'>
>>> set([4, 6, 4, 5])
{4, 5, 6}
>>> set(range(10))
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> 
>>> 
>>> 
>>> s1 = set(range(5))
>>> s2 = set(range(2))
>>> s1
{0, 1, 2, 3, 4}
>>> s2
{0, 1}
>>> s1.add('5')
>>> s1
{0, 1, 2, 3, 4, '5'}
>>> s1.intersection(s2)
{0, 1}
>>> s1&s2
{0, 1}
>>> s1.union(s2)
{0, 1, 2, 3, 4, '5'}
>>> s1|s2
{0, 1, 2, 3, 4, '5'}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> ()
()
>>> (5)
5
>>> (6,)
(6,)
>>> b = ('1', 1, '4')
>>> b[1]
1
>>> len(b)
3
>>> t = tuple(range(5))
>>> t
(0, 1, 2, 3, 4)
>>> t + b
(0, 1, 2, 3, 4, '1', 1, '4')
>>> (x, y) = (10, 5)
>>> x
10
>>> y
5
>>> x, y = 10, 5
>>> x
10
>>> y
5
>>> x, y = y, x
>>> x
5
>>> y
10
>>> t[1] = 'a'
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    t[1] = 'a'
TypeError: 'tuple' object does not support item assignment
>>> 
>>> 
>>> t = (1, [3, 6], 4)
>>> t[1][0] = 444
>>> t
(1, [444, 6], 4)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> eng2sp = dict()
>>> eng
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    eng
NameError: name 'eng' is not defined
>>> eng2sp
{}
>>> eng2sp['one'] = 'uno'
>>> eng2sp
{'one': 'uno'}
>>> eng2sp['one']
'uno'
>>> eng2sp['three'] = 'tres'
>>> eng2sp['two'] = 'dos'
>>> eng2sp
{'one': 'uno', 'two': 'dos', 'three': 'tres'}
>>> 'one' in eng2sp
True
>>> 'four' in eng2sp
False
>>> 
==================== RESTART: C:/Python projects/dict.py ====================
>>> qwertyuiqqqww
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    qwertyuiqqqww
NameError: name 'qwertyuiqqqww' is not defined
>>> 
==================== RESTART: C:/Python projects/dict.py ====================
>>> histogram('qwertyuqqqqwww[[[[[[[')
{'r': 1, 'w': 4, 't': 1, 'q': 5, 'u': 1, '[': 7, 'y': 1, 'e': 1}
>>> 
