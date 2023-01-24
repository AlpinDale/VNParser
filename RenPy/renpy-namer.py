import re

#Ask for the file name
filename = input("Enter the filename (including the file extension): ")

#open the text file
with open(filename, "r") as f:
    lines = f.read().splitlines()

#create a dictionary to store the speaker names and their replacement
speaker_names = {}

for i, line in enumerate(lines):
    match = re.match(r"([A-Za-z]+):", line)
    if match:
        speaker_abbr = match.group(1)
        if speaker_abbr not in speaker_names:
            correct_name = input("Enter the correct name for {} (press Enter without typing anything to skip): ".format(speaker_abbr))
            if correct_name:
                speaker_names[speaker_abbr] = correct_name
        if speaker_abbr in speaker_names:
            lines[i] = re.sub(r"^[A-Za-z]+:", speaker_names[speaker_abbr] + ":", line)

#write the modified lines back to the same file
with open(filename, "w") as f:
    for line in lines:
        f.write(line+'\n')
