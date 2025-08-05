# currency conversion with unpackaging and f-strings
data = [
    (100, "USD", 'EUR', 0.85),
    (100, "USD", 'CAD', 1.27),
    (100, 'CAD', 'EUR', 0.65)
]
# unpackaging and f-string formatting
for amount, from_currency, to_currency, rate in data:
    converted_amount = amount * rate
    print(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency} at a rate of {rate:.2f}")

# sum of odd numbers 1 to 100
s = 0
for i in range(1, 101):
    if i % 2 != 0:
        s += i
print("Sum of odd numbers from 1 to 100:", s)

# Number guessing game
number = 42
n_input = input("Guess the number (between 1 and 100): ")
guess = int(n_input)

while guess != number:
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    n_input = input("Guess the number (between 1 and 100): ")
    guess = int(n_input)

#Enumerate list item with index
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}, Length: {len(fruit)}")

# mutate the data
data = (['2021-01-01', 20, 10],
        ['2021-01-02', 20, 18],
        ['2021-01-03', 10, 10],
        ['2021-01-04', 102, 100],
        ['2021-01-05', 45, 25])

max_diff = None
max_date = None

for row in data:
    stop = row[1]
    start = row[2]
    diff = stop - start
    row.insert(1, diff)
    if max_diff is None or diff > max_diff:
        max_diff = diff
        max_date = row[0]

print("Date with largest difference:", max_date)
