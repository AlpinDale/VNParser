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
lines = [line for line in lines if not line.startswith("voice")]
lines = [line for line in lines if not line.startswith("stop")]
lines = [line for line in lines if not line.startswith("scene")]
lines = [line for line in lines if not line.startswith("with")]
lines = [line for line in lines if not line.startswith("show")]
lines = [line for line in lines if not line.startswith("hide")]
lines = [line for line in lines if not line.startswith("play")]
lines = [line for line in lines if not line.startswith("window")]
lines = [line for line in lines if not line.startswith("$")]
lines = [line for line in lines if not line.startswith("if")]
lines = [line for line in lines if not line.startswith("pause")]
lines = [line for line in lines if not line.startswith("label")]
lines = [line for line in lines if not line.startswith("call")]
lines = [line for line in lines if not line.startswith("return")]
lines = [line for line in lines if not line.startswith("jump")]
lines = [line for line in lines if not line.startswith("menu")]
lines = [line for line in lines if not line.startswith("    ")]
lines = [line for line in lines if not line.startswith("        ")]
lines = [line for line in lines if not line.startswith("elif")]
lines = [line for line in lines if not line.startswith("midget")]
lines = [line for line in lines if not line.startswith("]")]
lines = [line for line in lines if not line.startswith("[")]
lines = [line for line in lines if not line.startswith("queue")]

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


