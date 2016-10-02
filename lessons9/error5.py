try:
    i = int(input('Enter number: '))
    print(5 / i)
except ZeroDivisionError as z:
    print('Error! Dividing by zero')
    print(z)
except ValueError as v:
    print('Error! Converting to a number')
    print(v)
else:
    print('if no exceptions')
finally:
    print('always and last queue')
