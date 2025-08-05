# anagram
s1 = "listen"
s2 = "silent"

def letter_count(word):
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1
    return freq

dict1 = letter_count(s1)
dict2 = letter_count(s2)

are_anagrams = dict1 == dict2
print(f"Are '{s1}' and '{s2}' anagrams? {are_anagrams}")

dict1.pop('l', None)

print("dict1 after deleting 'l':", dict1)
print("dict2:", dict2)

# invert a dictionary with duplicates in values
grades = {"Alice": "A",
          "Bob": "B",
          "Charlie": "A",
          "Diana": "C"}
inverted_grades = {}
for student, grade in grades.items():
    if grade not in inverted_grades:
        inverted_grades[grade] = []
    inverted_grades[grade].append(student)
print("Inverted grades dictionary:", inverted_grades)

# set analysis for conference attendees
testing = {"Ana", "Bob", "Charlie", "Diana"}
development = {"Charlie", "Eve", "Frank", "Ana"}
devops = {"George", "Ana", "Bob", "Eve"}
# Find attendees who attended all three sessions
all_sessions = testing & development & devops
print("Attendees who attended all three sessions:", all_sessions)
# Find attendees who attended only one session
only_testing = testing - (development | devops)
print("Attendees who attended only the testing session:", only_testing)

# get a set of all unique attendees and sort them alphabetically
all_attendees = sorted(testing | development | devops)
print("All unique attendees sorted alphabetically:", all_attendees)

# create a copy of the development set and clear the original
dev_copy = development.copy()
development.clear()
print("Development set after clearing:", development)

#create data with comprehension
squares = [x**2 for x in range(1, 11)]
print("Squares:", squares)

div_by_7 = {x for x in range(1, 51) if x % 7 == 0}
print("Divisible by 7:", div_by_7)

score = {"Alice": 85, "Bob": 59, "Charlie": 92}
passed = {k: v for k, v in score.items() if v >= 60}
print("Passed students:", passed)

students = ["Michael", "David", "Liza"]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

attendance = {
    student: {day: (day in ["Mon", "Wed"]) for day in weekdays}
    for student in students
}
print("Attendance log:", attendance)
