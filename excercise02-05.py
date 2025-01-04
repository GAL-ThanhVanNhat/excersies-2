FILE_PATH = "mbox-short.txt"

file = open(FILE_PATH, 'r')
result = {}

for line in file:
    if not line.startswith("From "):
       continue
    else:
        words = line.split(":")
        #print(words)
        hour = words[0][-2:]
        if hour not in result:
            result[hour] = 1
        else:
            result[hour] += 1
            
result = sorted(result.items())       
print(result)