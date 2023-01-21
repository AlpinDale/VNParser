import glob
import os

directory = '/path/to/your/directory/'
rpy_files = sorted(glob.glob(directory + '*.rpy'))
combined_file = open(directory + 'combined.rpy', 'w')
for filename in rpy_files:
    with open(filename) as f:
        for line in f:
            combined_file.write(line)
combined_file.close()
