KEY = "X-DSPAM-Confidence:"
FILE_PATH = "mbox.txt"

file =  open(FILE_PATH, 'r')
confidence_array = []

for line in file:
    if line.startswith(KEY):
        confidence = float(line.split(':')[1].strip())
        confidence_array.append(confidence)
    else:
        continue
    
result = sum(confidence_array)/len(confidence_array)
print(result)