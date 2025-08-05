# file filtering with context manager

with open('students.txt', 'w') as f:
    f.write('Alice\nEve\nOscar\nUma\nBob\nCharlie\nIan\n')

vowels = ('A', 'E', 'I', 'O', 'U')
with open('students.txt', 'r') as infile, open('filtered.txt', 'w') as outfile:
    for line in infile:
        name = line.strip()
        if name and name[0].upper() in vowels:
            outfile.write(name + '\n')


# reverse file content
with open('log.txt', 'w') as f:
    f.write('line 1\nline 2\nline 3\nline 4\nline 5\n')

with open('log.txt', 'r') as infile, open('reversed_log.txt', 'w') as outfile:
    lines = infile.readlines()
    for line in reversed(lines):
        outfile.write(line)

# modularize student report generator

from report import generate_report

data = {'Lisa': 85, 'Bart': 72, 'Homer': 91}
report = generate_report(data)
print(report)