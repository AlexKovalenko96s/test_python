try:
    i = int(input('Enter number: '))
    print(5 / i)
except ZeroDivisionError:
    print('Error! Dividing by zero')
except ValueError:
    print('Error! Converting to a number')
