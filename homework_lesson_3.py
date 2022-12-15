# task 1
student = int(input("Enter schoolboys count: "))
apples = int(input("Enter apples count: "))

print(f"Each student will receive {int(apples / student)} apple(s) and {apples % student} apple(s) left in basket\n")


# task 2
students_in_room_one = int(input("Enter students count in room 1: "))
students_in_room_two = int(input("Enter students count in room 2: "))
students_in_room_three = int(input("Enter students count in room 3: "))

print(f"First room with {students_in_room_one} students need {students_in_room_one // 2 + students_in_room_one % 2} "
      f"tables")
print(f"Second room with {students_in_room_two} students need {students_in_room_two // 2 + students_in_room_two % 2} "
      f"tables")
print(f"Third room with {students_in_room_three} students need "
      f"{students_in_room_three // 2 + students_in_room_three % 2} tables\n")


# task 3
single_number = int(input('Input number: '))  # variable for input and units
decimal_number = single_number  # variable for decimals
hundred_number = single_number  # variable for hundreds

# operations with digits
single_number %= 10
decimal_number %= 100
decimal_number //= 10
hundred_number //= 100

print(f"Reversed number is: {single_number * 100 + decimal_number * 10 + hundred_number}\n")


#task 4
input_var = int(input('Enter seconds: '))
seconds = input_var % 60
minutes = input_var / 60 % 60
hours = input_var / 60 / 60 % 60

print(f"Time is: {int(hours)}:{int(minutes)}:{int(seconds)}")

