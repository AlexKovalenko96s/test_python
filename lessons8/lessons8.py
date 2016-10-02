Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> num = [1, 2, 3, 4, 69, 96]
>>> num
[1, 2, 3, 4, 69, 96]
>>> for i in num:
	print(i, 'number')

	
1 number
2 number
3 number
4 number
69 number
96 number
>>> 
>>> country = "Ukraine"
>>> country
'Ukraine'
>>> for ch in country:
	if ch.isupper():
		print(cr)

		
Traceback (most recent call last):
  File "<pyshell#11>", line 3, in <module>
    print(cr)
NameError: name 'cr' is not defined
>>> for ch in country:
	if ch.isupper():
		print(ch)

		
U
>>> range(10)
range(0, 10)
>>> for i in range(10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(1,11))
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(range(1, 11, 2))
[1, 3, 5, 7, 9]
>>> list(range(11, 1, -2))
[11, 9, 7, 5, 3]
>>> 
>>> 
>>> 
>>> total = 0
>>> for i in range(1, 101):
	total += i

	
>>> total
5050
>>> sum(list(range(1, 101)))
5050
>>> 
>>> 
>>> 
>>> 
>>> v = [4, 10, 5, 7.5, -5.9]
>>> v
[4, 10, 5, 7.5, -5.9]
>>> for i in range(len(v)):
	v[i] = v[i] * 2
	print('v[', i, ']', '=', v[i])

	
v[ 0 ] = 8
v[ 1 ] = 20
v[ 2 ] = 10
v[ 3 ] = 15.0
v[ 4 ] = -11.8
>>> v
[8, 20, 10, 15.0, -11.8]
>>> 
>>> 
>>> 
>>> 
>>> out = [1, 2, 3, 4]
>>> into = [5, 6, 7, 8]
>>> for i out:
	
SyntaxError: invalid syntax
>>> for i in out:
	for j in into:
		print('i =', i, 'j =', j)

		
i = 1 j = 5
i = 1 j = 6
i = 1 j = 7
i = 1 j = 8
i = 2 j = 5
i = 2 j = 6
i = 2 j = 7
i = 2 j = 8
i = 3 j = 5
i = 3 j = 6
i = 3 j = 7
i = 3 j = 8
i = 4 j = 5
i = 4 j = 6
i = 4 j = 7
i = 4 j = 8
>>> 
>>> 
>>> 
>>> 
>>> lst = [[1, 2, 3], [4, 5, 6]]
>>> for i in lst:
	print(i)

	
[1, 2, 3]
[4, 5, 6]
>>> for i in lst:
	for j in i:
		print(j)

		
1
2
3
4
5
6
>>> 
>>> 
>>> 
>>> 
>>> rabbits = 3
>>> while rabbits > 0:
	print(rabbits)
	rabbits -= 1

	
3
2
1
>>> 
>>> 
>>> 
>>> text = ''
>>> while text != "stop":
	text = input('Enter number or stop: ')
	if text == 'stop':
		print('Exit')
	elif text == '1':
		print('Number = 1')
	else:
		print('What fuck is this?')

		
Enter number or stop: ddd
What fuck is this?
Enter number or stop: 1
Number = 1
Enter number or stop: stop
Exit
>>> while True:
	text = input('Enter number or stop: ')
	if text == 'stop':
		print('Exit')
		break
	elif text == '1':
		print('Number = 1')
	else:
		print('What fuck is this?')

		
Enter number or stop: dddd
What fuck is this?
Enter number or stop: 1
Number = 1
Enter number or stop: stop
Exit
>>> 
>>> 
>>> 
>>> s = 'qwe3gfdgt6ff'
>>> total = 0
>>> for i in range(len(s)):
	if s[i].isalpha():
		continue
	total += int(s[i])

	
>>> total
9
>>> 
