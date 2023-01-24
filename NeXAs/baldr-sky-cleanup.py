import re

file_name = input("Enter the file name (with extension): ")

with open(file_name, 'r') as f:
    lines = f.readlines()

new_lines = []

for line in lines:
    line = re.sub(r'\\t\S{4}', '', line)
    line = re.sub(r'\\s\S{4}', '', line)
    line = re.sub(r'\\s\S{2}', '', line)
    line = re.sub(r'\\r\\', '', line)
    line = re.sub(r'\\h(KOU|RAIN|CHINATSU|NANOHA|MAKOTO|SORA|AKI|SEIRA|KUU|ANAN|GILBERT|EIJI|ISAO|NAOKI|NOI|SHIZEL|MASA)\S{6}', '', line)
    new_lines.append(line)

with open(file_name, 'w') as f:
    for line in new_lines:
        f.write(line)

# remove remaining instances of \t, \h, and \r
with open(file_name, 'r') as f:
    lines = f.read()

lines = lines.replace("\h", "")
lines = lines.replace("\r", "")
lines = lines.replace("\t", "")
lines = lines.replace("\s", "")

with open(file_name, 'w') as f:
    f.write(lines)

