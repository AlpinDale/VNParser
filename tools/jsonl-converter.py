import json
import glob

output_file = 'output.jsonl'
text_files = glob.glob('*.txt*')

for file in text_files:
    with open(file) as f:
        for line in f:
            obj = {'text': line.strip()}
            with open(output_file, 'a') as out_f:
                out_f.write(json.dumps(obj) + '\n')
