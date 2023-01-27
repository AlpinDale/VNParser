import re
import os

def script1(file_name):
    with open(file_name, "r") as f:
        text = f.read()
    text = re.sub(r'</PRE>|<PRE[^\n]*\]', '', text, flags=re.MULTILINE)
    with open(file_name, "w") as f:
        f.write(text)

def script2(file_name):
    with open(file_name, "r") as f:
        with open("cleaned_" + file_name, "w") as out:
            for line in f:
                if not re.match(r'\*</PRE>|\*<PRE[^\n]*\]', line):
                    out.write(line)
def remove_color_codes(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    with open(file_name, "w") as f:
        for line in lines:
            if not re.search(r'#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3}', line):
                f.write(line)

file_name = input("Please enter the input file name: ")
if os.path.isfile(file_name):
    script1(file_name)
    with open(file_name, "r") as f:
        # Open the output file
        with open("output.txt", "w") as out:
            speaker = ""
            for line in f:
                # Extract the speaker names
                new_speaker = re.search(r'<voice name="([^"]*)"', line)
                if new_speaker:
                    speaker = new_speaker.group(1)
                    continue
                # Extract the dialogues
                dialogue = re.search(r'"([^"]*)"', line)
                if dialogue:
                    out.write(speaker + ": " + dialogue.group(1) + "\n")
                    continue
                if line.strip():
                    # Enclose the regular text in asterisks
                    line = "*" + line.rstrip() + "*\n"
                    out.write(line)
    script2("output.txt")
    os.remove("output.txt") # This line will delete the file named "output.txt" after everything is executed
    remove_color_codes("cleaned_output.txt")
else:
    print(f"{file_name} not found!")
