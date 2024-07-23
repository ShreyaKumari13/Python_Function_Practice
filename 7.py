''' 
    7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
    Sample String : 'The quick Brow Fox'
    Expected Output :
    No. of Upper case characters : 3
    No. of Lower case Characters : 12
'''
def low_upp(str1):
    count1 = 0
    count2 = 0
    for i in str1:
        if (i>="a" and i<="z"):
            count1+=1
        elif(i>="A" and i<="Z"):
            count2+=1
    print('No. of Lower case Characters :',count1)
    print('No. of Upper case characters :',count2)
str1 = 'The quick Brow Fox'
low_upp(str1)