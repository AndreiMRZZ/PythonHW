# List
numbers = [10, 20, 30, 40, 50]
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Middle element:", numbers[len(numbers) // 2])

# add a new element
numbers.append(60)
print("After adding 60:", numbers)

# insert 15 at index 1
numbers.insert(1, 15)

# remove the last element
numbers.pop()
print("Length of the list:", len(numbers))

#sort the list
numbers.sort()
print("Sorted list:", numbers)

# Change specific word in a sentence without using replace
sentence = "Python is fun because Python is powerful"
target_word = "Python"
new_word = "Programming"

words = sentence.split()
modified_words = [new_word if word == target_word else word for word in words]
modified_sentence = " ".join(modified_words)

print("Original sentence:", sentence)
print("Modified sentence:", modified_sentence)

# palindrome check with slicing
s = ("radar")
if s == s[::-1]:
    print(f"{s} is a palindrome")
else:
    print(f"{s} is not a palindrome")

# f-string formatting
name = "Alice"
age = 30
balance = 1234.56789
membership_date = "2023-08-12"
staus = True

print(f"Name: {name}, Age: {age}, Balance: ${balance:.2f}, Membership Date: {membership_date}, Status: {'Active' if staus else 'Inactive'}")