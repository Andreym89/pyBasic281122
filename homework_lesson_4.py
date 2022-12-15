#task 1

user_choice = int(input('Chone oprations:\n1."+"\n2."-"\n3."*"\n4."/"\n5."**"\n'))


if user_choice == 1:
    first_addend_number = float(input('You chose "+"\nInput fist digit: '))
    second_addend_number = float(input('Input fist digit: '))
    print(f'Result: {first_addend_number+second_addend_number}')
elif user_choice == 2:
    first_number = float(input('You chose "-"\nInput fist digit: '))
    second_number = float(input('Input fist digit: '))
    print(f'Result: {first_number + second_number}')
elif user_choice == 3:
    first_number = float(input('You chose "*"\nInput fist digit: '))
    second_number = float(input('Input fist digit: '))
    print(f'Result: {first_number * second_number}')
elif user_choice == 4:
    first_number = float(input('You chose "/"\nInput fist digit: '))
    second_number = float(input('Input fist digit: '))
    if second_number == 0:
        print("Result: undefined")
    else:
        print(f'Result: {first_number / second_number}')
elif user_choice == 5:
    first_number = float(input('You chose "**"\nInput fist digit: '))
    second_number = float(input('Input fist digit: '))
    print(f'Result: {first_number ** second_number}')
else:
    pass
#task 2

#task 3

#task *

print('Маша нашла в лесу {K} гриб...', end='')
