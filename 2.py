'''
    2. Write a Python function to sum all the numbers in a list.
    Sample List : (8, 2, 3, 0, 7)
    Expected Output : 20
'''
def sum1(list1):
    sum2 = 0
    for i in list1:
        sum2+=i
    return sum2
list1 = [8, 2, 3, 0, 7]
print(sum1(list1))