'''
    10. Write a Python program to print the even numbers from a given list.
    Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
    Expected Result : [2, 4, 6, 8]
'''
def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def is_even_num(l):
    for n in l:
        if n % 2 != 0:
            l.remove(n)
    return l
print(is_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))

