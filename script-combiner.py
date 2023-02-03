import glob
import os

directory = './'
extension = input("Enter the extension of the files you want to combine (e.g. '.txt' or '.rpy'): ")
files = sorted(glob.glob(directory + '*' + extension))
combined_file = open(directory + 'combined' + extension, 'w')
for filename in files:
    separator = '\n' + '\n' * 5 + '=' * 10 + os.path.basename(filename) + '=' * 10 + '\n'
    combined_file.write(separator)
    with open(filename) as f:
        for line in f:
            combined_file.write(line)
    combined_file.write('\n' * 5)
combined_file.close()
