import re

filename = input("Enter the filename (with extension): ")

with open(filename, "r") as f:
    lines = f.read().splitlines()


#remove lines that don't start with 4 spaces
lines = [line for line in lines if line.startswith("    ")]

for i, line in enumerate(lines):
    #remove 4 spaces from the start of the line
    lines[i] = line[4:]
    if re.match(r"^\".*\"", lines[i]):
        lines[i] = re.sub(r"^\"|\"$", "*", lines[i])
    elif not re.match(r"^\*.*\*", lines[i]):
        # lines [i] = re.sub(r"(\b[a-z])", lambda x: x.group(1).upper(), lines[i])
        lines[i] = re.sub(r"^([A-Za-z]+)(.*)", r"\1: \2", lines[i])

# write the modified lines to the output file
with open("output.txt", "w") as f:
    for line in lines:
        f.write(line+'\n')

# open the output for final modifications

with open("output.txt", "r") as f:
    lines = f.read().splitlines()

# remove renpy command lines
RENPY_CMD_LINES = ("voice", "stop", "scene", "with", "show", "hide", "queue", "play", "window", "$", "else", "if", "pause", "label", "call", "return", "jump", "menu", "    ", "        ", "elif", "midget", "]", "[", "queue", "xalign", "yalign", "#", "fixed", "imagemap", "imagebutton", "default", "linear", "xpos", "python")
lines = [line for line in lines if not line.startswith(RENPY_CMD_LINES)]

for i, line in enumerate(lines):
    # remove all instances of backslash in the file
    lines[i] = line.replace( "\\", "")

# write the modifications to the output file
with open("output.txt", "w") as f:
    for line in lines:
        f.write(line+'\n')

# print the output file again

with open("output.txt", "r") as f:
    print(f.read())

f.close()


