Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> e = [56, 57, 58, 59]
>>> e[0]
56
>>> e.index(56)
0
>>> k = ['Hi', 27, -6.8, [1, 2]]
>>> k
['Hi', 27, -6.8, [1, 2]]
>>> k[0] = 'noHi'
>>> k
['noHi', 27, -6.8, [1, 2]]
>>> k.len()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    k.len()
AttributeError: 'list' object has no attribute 'len'
>>> len(k)
4
>>> max(e)
59
>>> min(e)
56
>>> sum(e)
230
>>> sorted(e)
[56, 57, 58, 59]
>>> original = ['H', 'B']
>>> final = original + ['T']
>>> final
['H', 'B', 'T']
>>> final = final * 5
>>> final
['H', 'B', 'T', 'H', 'B', 'T', 'H', 'B', 'T', 'H', 'B', 'T', 'H', 'B', 'T']
>>> del final[0]
>>> final
['B', 'T', 'H', 'B', 'T', 'H', 'B', 'T', 'H', 'B', 'T', 'H', 'B', 'T']
>>> 
>>> 
>>> h = ['Hi', 7, 'privrt', -1.0, 'say hello']
>>> h
['Hi', 7, 'privrt', -1.0, 'say hello']
>>> if 7 in h:
	print('in list')

	
in list
>>> h1 = ['say hello', 7]
>>> h1
['say hello', 7]
>>> if h1 in h:
	print('yes')

	
>>> g = h[1:2]
>>> g
[7]
>>> klon = h[:]
>>> klon
['Hi', 7, 'privrt', -1.0, 'say hello']
>>> h[1] = 8
>>> h
['Hi', 8, 'privrt', -1.0, 'say hello']
>>> klon
['Hi', 7, 'privrt', -1.0, 'say hello']
>>> klon2 = h
>>> klon2
['Hi', 8, 'privrt', -1.0, 'say hello']
>>> h[1] = 9
>>> h
['Hi', 9, 'privrt', -1.0, 'say hello']
>>> klon2
['Hi', 9, 'privrt', -1.0, 'say hello']
>>> 
>>> 
>>> 
>>> colors = ['red', 'orange', 'green']
>>> colors
['red', 'orange', 'green']
>>> colors.extend(['black', 'blue'])
>>> colors
['red', 'orange', 'green', 'black', 'blue']
>>> colors.append('purple')
>>> colors
['red', 'orange', 'green', 'black', 'blue', 'purple']
>>> colors.insert(2, 'yellow')
>>> colors
['red', 'orange', 'yellow', 'green', 'black', 'blue', 'purple']
>>> colors.remove('black')
>>> colors
['red', 'orange', 'yellow', 'green', 'blue', 'purple']
>>> colors.count('red')
1
>>> colors.index('green')
3
>>> colors
['red', 'orange', 'yellow', 'green', 'blue', 'purple']
>>> colors.pop()
'purple'
>>> colors
['red', 'orange', 'yellow', 'green', 'blue']
>>> colors.reverse()
>>> colors
['blue', 'green', 'yellow', 'orange', 'red']
>>> colors.sort()
>>> colors
['blue', 'green', 'orange', 'red', 'yellow']
>>> colors.clear()
>>> colors
[]
>>> n = 123456789
>>> list(str(n))
['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> s = 'd a dd dd gg rr tt yy rr ee'.split()
>>> s
['d', 'a', 'dd', 'dd', 'gg', 'rr', 'tt', 'yy', 'rr', 'ee']
>>> 
>>> 
>>> lst = [['A', 1], ['B', 2], ['C', 3]]
>>> lst
[['A', 1], ['B', 2], ['C', 3]]
>>> lst[0]
['A', 1]
>>> lst[0][1]
1
>>> 
