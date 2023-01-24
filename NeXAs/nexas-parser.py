import re

def check_word(string):
    return bool(re.match(r"^[a-zA-Z]+$", string.strip()))

file_name = input("Enter the file name (with extension): ")

with open(file_name, 'r') as f:
    lines = f.readlines()

new_lines = []

for i, line in enumerate(lines):
    if i != len(lines) - 1:
        word = line.strip().split()
        if len(word) == 1 and check_word(word[0]):
            new_line = word[0] + ": " + lines[i + 1].strip()
            new_lines.append(new_line)
            continue
    else:
        new_lines.append(line.strip())

with open(file_name, 'w') as f:
    for line in new_lines:
        f.write(line + '\n')
