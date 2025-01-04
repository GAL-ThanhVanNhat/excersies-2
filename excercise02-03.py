FILE_PATH = "romeo.txt"

file = open(FILE_PATH, 'r')
result = []

for line in file:
    words = line.split()
    for word in words:
        if word not in result:
            result.append(word)
        else:
            continue

result.sort()
print(result)
