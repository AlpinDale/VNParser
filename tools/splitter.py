import random 
 
fin = open("/path/to/input.json", 'rb') 
f75out = open("/path/to/80-percent.json", 'wb') 
f25out = open("/path/to/20-percent.json", 'wb') 
for line in fin: 
    r = random.random() 
    if r < 0.80: 
        f80out.write(line) 
    else: 
        f20out.write(line) 
fin.close() 
f80out.close() 
f20out.close()
