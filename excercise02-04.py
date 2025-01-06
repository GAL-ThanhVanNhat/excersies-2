FILE_PATH = "mbox-short.txt"
KEY = "Author"

file = open(FILE_PATH, 'r')
result = {}

for line in file:
    if not line.startswith(KEY):
       continue
    else:
        words = line.split(":")
        email = words[1].strip()
        if email not in result:
            result[email] = 1
        else:
            result[email] += 1
           
print(result)