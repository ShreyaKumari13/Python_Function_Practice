'''
    6. Write a Python function to check whether a number falls in a given range.
'''
def ran(n):
    if n in range(1,9):
        print('%d is in the range'%n)
    else:
        print('%d is not in the range'%n)
ran(3)
ran(5)
ran(7)
ran(9)
ran(11)
ran(13)