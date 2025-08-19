from math import *
n = int(input('Enter a number to count the digits: ')) 

num = n # not changing the input if not mentioned

def countDigits(num):
    return int(log10(num)+1)

#testing the func
print(f'the number',n,'includes',countDigits(num),'digti(s)')