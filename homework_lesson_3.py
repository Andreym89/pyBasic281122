#task 1
#task 2


#task 3
single_number = int(input('Input number: '))   # variable for input and units
decimal_number = single_number       # variable for decimals
hundred_number = single_number       # variable for hundreds
#
single_number %= 10
decimal_number %= 100
decimal_number //= 10
hundred_number //= 100

print(f"Reversed number is: {single_number*100 + decimal_number*10 + hundred_number}")
