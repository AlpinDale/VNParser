import sys
import re

try:
    filename = sys.argv[1]
except IndexError:
    print("Error: No filename specified.")
    sys.exit()

with open(filename, "r") as f:
    lines = f.read().splitlines()

for i, line in enumerate(lines):
    while "[" in line and "]" in line:
        start = line.find("[")
        end = line.find("]")
        line = line[:start] + line[end+1:]
    lines[i] = line

with open(filename, "w") as f:
    for line in lines:
        f.write(line + '\n')
