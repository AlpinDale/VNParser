## VNParser
This project is created to build a universal script that can take raw scripts from Visual Novels (extracting the script from the VN is beyond the scope of this project) and outputting them in a clean format, to be used in training AI.

# Current scripts:
- Steins;Gate
- RenPy
- NeXAs
- rUGP

`jpn-remover.py` removes any instance of Japanese text from a file.
`square-bracket-remover.py` finds all instances of strings of characters enclosed in square brackets, such as font indicators etc, and removes them.

### Note:
Due to the nature of VNs, the formatting might differ even on VNs from the same engine. You may have to manually look through the finished product and check for any problems. Most likely, it won't be a problem.

### RenPy note:
Look through your raw script and see if dialogues start after 4 spaces in a new line. If they do, the script will work. Otherwise, you'll have to make modifications to the script to make it work.

### NeXAs note:
Only tested on Baldr Sky. Needs more testing with other games.
