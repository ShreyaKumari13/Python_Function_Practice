'''
    1. Write a Python function to find the Max of three numbers.
'''
def max_of(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    else :
        return c
print(max_of(3,2,4))
