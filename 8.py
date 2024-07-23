'''
    8. Write a Python function that takes a list and returns a new list with unique elements of the first list.
    Sample List : [1,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]
'''
# def unique(list1):
#     return set(list1)
# list1 = [1,2,3,3,3,3,4,5]
# print(list(unique(list1)))

def unique_list(l):
  x = []
  for i in l:
    if i not in x:
      x.append(i)
  return x
print(unique_list([1,2,3,3,3,3,4,5])) 


