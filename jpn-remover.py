import re

file_name = input("Enter the file name (with extension): ")

with open(file_name, 'r') as f:
    lines = f.readlines()

new_lines = []

for line in lines:
    new_line = re.sub(r'[\u3040-\u309f\u30a0-\u30ff\u4e00-\u9faf]', '', line) # remove all Japanese characters
    new_lines.append(new_line)

with open(file_name, 'w') as f:
    for line in new_lines:
        f.write(line)

