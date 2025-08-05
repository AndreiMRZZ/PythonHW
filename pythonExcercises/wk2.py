# 1 Immutable
# Integer example
a = 10
print("Integer before change:", a, "id:", id(a))
a += 5
print("Integer after change:", a, "id:", id(a))

# Float example
b = 3.14
print("Float before change:", b, "id:", id(b))
b *= 2
print("Float after change:", b, "id:", id(b))

# Leap Year Check
year_str = input("Enter desired year: ")
year = int(year_str)
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#Ternary conditional operator
num = 5
print("Positive" if num > 0 else "Negative")

#Boolean logic
x = 5
y = 0
z = -3

# 1. Check if all three numbers are greater than zero
print("All greater than zero:", x > 0 and y > 0 and z > 0)

# 2. Check if at least one number is equal to zero
print("At least one is zero:", x == 0 or y == 0 or z == 0)

# 3. Check if none of the numbers are negative
print("None are negative:", not (x < 0 or y < 0 or z < 0))


#Type conversion
x = 100
y = -30
z = 0

# Convert to float
x_float = float(x)
y_float = float(y)
z_float = float(z)
print("Converted to float:")
print("x:", x_float, "y:", y_float, "z:", z_float)

# Convert to string
x_str = str(x)
y_str = str(y)
z_str = str(z)
print("Converted to string:")
print("x:", x_str, "y:", y_str, "z:", z_str)

# Convert to boolean
x_bool = bool(x)
y_bool = bool(y)
z_bool = bool(z)
print("Converted to boolean:")
print("x:", x_bool, "y:", y_bool, "z:", z_bool)