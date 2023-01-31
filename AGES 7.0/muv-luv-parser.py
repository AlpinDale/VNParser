file_name = input("Enter the file name: ")

with open(file_name, "r", encoding='utf-8') as file:
    content = file.readlines()

with open(file_name, "w", encoding='utf-8') as file:
    for line in content:
        if line.startswith("//") or line.startswith("#") or line.startswith(" \r") or not line.strip() or "\\b" in line or "//lit" in line or "//" in line:
            continue
        line = line.replace("<", "").replace(">", "")
        line = line.replace("\\p", "").replace("\\e", "")
        line = line.replace("【", "")
        line = line.replace("】", ":")
        line = line.lstrip()
        line = line.replace("「", " \"").replace("」", "\"")
        line = line[9:]
        if line.startswith("\\"):
            continue
        file.write(line)
