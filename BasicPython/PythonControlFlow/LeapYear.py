year = int(input('Which year  do you went to check? '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f'the {year} is a leap year')
        else:
            print(f'{year} is not leap year')
    else:
        print(f'the {year} is a leap year')
else:
    print(f'{year} is not leap year')
