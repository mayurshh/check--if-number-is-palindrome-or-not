n = int(input('Enter a number to Check IF its Armstrong or Not: '))
no_of_digits = len(str(n))
total = 0
num = n

while num > 0:
    ld = num % 10 
    total = total + (ld ** no_of_digits)
    num = num // 10
if total == n:
    print('YES the number entered is Armstrong.')
else:
    print('NO the number entered isnt armstrong')
