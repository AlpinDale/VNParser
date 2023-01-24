## NeXAs Note:
Run the script `nexas-parser` with python to clean up the formatting. 
Run the script `baldr-sky-cleanup` to remove characters the parsing script couldn't remove.

I uploaded the cleanup script separately because it will be different for each game. If the game isn't Baldr's Sky,
look for any instances of `\h` in the file and take note of the capitalized letters that follow it - these are the character names.
Then open up the `baldr-sky-cleanup` file and replace the names in line 13 with the ones you've found. Then you can run the script.

## IMPORTANT
The script doesn't seem to delete instances of `\t` and `\n` at the end. I don't know the reason for the first one, but for `\n` it's
impossible to my knowledge, because that would delete every line break too. So you have to open a text editor and replace all instances
of `\t` and `\n` with a blank character. You can do this by not typing anything in the replace section.
Also, it seems like Baldr's Sky has this weird character in the text: , make sure to remove it as well. Copy it here and paste in replace
screen.
