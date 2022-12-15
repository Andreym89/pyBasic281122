# task 1

user_choice = int(input('Task 1\nChose oprations:\n1."+"\n2."-"\n3."*"\n4."/"\n5."**"\n'))

if user_choice == 1:
    first_addend_number = float(input('You chose "+"\nInput fist number: '))
    second_addend_number = float(input('Input fist number: '))
    print(f'Result: {first_addend_number + second_addend_number}')
elif user_choice == 2:
    first_number = float(input('You chose "-"\nInput fist number: '))
    second_number = float(input('Input fist number: '))
    print(f'Result: {first_number - second_number}')
elif user_choice == 3:
    first_number = float(input('You chose "*"\nInput fist number: '))
    second_number = float(input('Input fist number: '))
    print(f'Result: {first_number * second_number}')
elif user_choice == 4:
    first_number = float(input('You chose "/"\nInput fist number: '))
    second_number = float(input('Input fist number: '))
    if second_number == 0:
        print("Result: undefined")
    else:
        print(f'Result: {first_number / second_number}')
elif user_choice == 5:
    first_number = float(input('You chose "**"\nInput fist number: '))
    second_number = float(input('Input fist number: '))
    print(f'Result: {first_number ** second_number}')
else:
    pass

# task 2

n_number = int(input('\nTask 2\nReturn full list of prime squares up to: '))
for i in range(int(n_number)):
    if (i + 1) ** 2 <= n_number:
        print((i + 1) ** 2, end=' ')

# task 3
divide_counter = 0
input_number = int(input('\n\nTask 3\nPrime number checker\nEnter your number: '))

if input_number == 0:
    print('You entered a prime number')
else:
    for i in range(1, int(input_number / 2)):
        if input_number % i == 0:
            divide_counter += 1
    if divide_counter > 1:
        print('You entered NOT a prime number')
    else:
        print('You entered a prime number')
