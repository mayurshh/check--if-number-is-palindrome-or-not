n = int(input('Enter a number to count the digits: '))

num = n # not changing the input if not mentioned
count = 0 #starting count 

while num > 0:
    count += 1
    num = num//10 
print(f'The number', n, 'includes', count,'digit(s)')
