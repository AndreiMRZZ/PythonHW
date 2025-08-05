# #create custom calculator with functions
# def calculate(*args, operation='+'):
#     if not args:
#         return 0
#
#     if operation == '+':
#         result = sum(args)
#     elif operation == '-':
#         result = args[0]
#         for num in args[1:]:
#             result -= num
#     elif operation == '*':
#         result = 1
#         for num in args:
#             result *= num
#     elif operation == '/':
#         result = args[0]
#         for num in args[1:]:
#             if num == 0:
#                 return 'Error: Division by zero'
#             result /= num
#     else:
#         return 'Error: Unsupported operation'
#     return result
#
# print(calculate(2, 3, 4, operation='*'))
# print(calculate(10, 0, operation='/'))
# print(calculate(operation='-'))

# # sort students by score using lambda
# names = ["Lucas", "Nataly", "Megi", "Maria", "Steven"]
# scores = [85, 92, 78, 81, 67]
#
# # Combine, filter, and sort
# students = list(zip(names, scores))
# filtered_sorted = sorted(
#     filter(lambda x: x[1] >= 80, students),
#     key=lambda x: x[1],
#     reverse=True
# )
#
# print(filtered_sorted)

# # validate age input
# def check_age(age):
#     try:
#         if age == '':
#             raise ValueError("Input cannot be empty.")
#         age_int = int(age)
#         if age_int < 0 or age_int > 120:
#             raise ValueError("Age must be between 0 and 120.")
#         print(f"Valid age: {age_int}")
#     except ValueError as ve:
#         print(f"ValueError: {ve}")
#     except TypeError:
#         print("TypeError: Invalid type for age input.")
#     finally:
#         print("Validation complete")
#
#
# check_age("25")
# check_age("-5")
# check_age("abc")
# check_age("")
# check_age("130")