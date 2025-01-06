KEY = "X-DSPAM-Confidence:"
FILE_PATH = "mbox.txt"

file =  open(FILE_PATH, 'r')
confidence_array = []

for line in file:
    if not line.startswith(KEY):
        continue
    else:
        confidence = float(line.split(':')[1].strip())
        confidence_array.append(confidence)
    
result = sum(confidence_array)/len(confidence_array)
print(result)