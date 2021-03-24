
for numbers in range(0, 100):
    if numbers % 3 == 0:
        print(numbers, 'Fizz')
for numbers in range(0, 100):
    if numbers % 5 == 0:
        print(numbers, 'buzz')
for numbers in range(0, 100):
    if numbers % 3 == 0 or numbers % 5 == 0:
        print(numbers, 'Fizzbuzz')
