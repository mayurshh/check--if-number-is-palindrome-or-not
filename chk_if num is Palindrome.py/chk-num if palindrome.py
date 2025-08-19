n =int(input('Enter a number to check if it is Palindrome  OR Not :'))
num = n
result = 0
while num >0:
    ld =num%10
    result = (result *10) +ld
    num = num // 10

if n ==result :
        print('Number is Palindrome')
else:
        print('Numbner is not Palindrome')
