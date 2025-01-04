FILE_PATH = "mbox-short.txt"

file = open(FILE_PATH, 'r')
result = {}

for line in file:
    if not line.startswith("Author"):
       continue
    else:
        words = line.split(":")
        email = words[1].strip()
        if email not in result:
            result[email] = 1
        else:
            result[email] += 1
           
print(result)