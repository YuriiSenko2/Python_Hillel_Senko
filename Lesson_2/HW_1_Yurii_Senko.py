from math import pi

# TASK 1
# 1.1. Ask for first and last name and display them

first_name = input('Your first name: ')
second_name = input('Your second name: ')
full_name = first_name + " " + second_name
print("User's full name:" + " " + full_name)

# 1.2. Upper,lower and capitalize

print("User's full name:" + " " + first_name.upper() + " " + second_name.upper())
print("User's full name:" + " " + first_name.lower() + " " + second_name.lower())
print("User's full name:" + " " + first_name.capitalize() + " " + second_name.capitalize())

# 1.3. Print a name for 5 times in a row

print((first_name + " " + second_name + "; ") * 5)

# 1.4. Remove blanks

new_full_name = "\t\t\t" + first_name + "\t\n\t" + second_name + "\t\t\n\t"
full_name = new_full_name
print(full_name)
full_name = full_name.strip()
full_name = full_name.replace("\t\n\t", " ")
print(full_name)

# TASK 2 - Length and area of the circle

radius = float(input('Input the radius: '))
circle_length = 2 * pi * radius
circle_area = pi * radius ** 2
print(f"Length of a circle = {circle_length}; \nArea of a circle = {circle_area} ")

# TASK 3 - Currency exchange

exchange_rate = float(input('Current exchange rate of hryvnia to the dollar: '))
dollar_amount = float(input('Amount of dollars to exchange: '))
uah_amount = dollar_amount * exchange_rate
uah_amount = uah_amount.__round__(2)
print(f"Amount of UAH to receive = {uah_amount}")

