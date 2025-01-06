FILE_PATH = "romeo.txt"

file = open(FILE_PATH, 'r')
result = []

for line in file:
    words = line.split()
    for word in words:
        if word in result:
            continue
        else:
            result.append(word)

result.sort()
print(result)
