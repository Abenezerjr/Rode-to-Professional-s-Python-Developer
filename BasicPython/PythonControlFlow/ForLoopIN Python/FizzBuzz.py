n = range(1, 21)

for i in n:
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print(f"Fizz")
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
