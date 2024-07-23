'''
    3. Write a Python function to multiply all the numbers in a list.
    Sample List : (8, 2, 3, -1, 7)
    Expected Output : -336
'''
def mul1(list1):
    mul = 1
    for i in list1:
        mul*=i
    return mul
list1 = [8, 2, 3, -1, 7]
print(mul1(list1))