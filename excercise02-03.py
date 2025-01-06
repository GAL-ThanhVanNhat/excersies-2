FILE_PATH = "romeo.txt"

def get_unique_words(file_path) -> list:
    file = open(file_path, 'r')
    result = []

    for line in file:
        words = line.split()
        for word in words:
            if word in result:
                continue
            else:
                result.append(word)

    result.sort()
    file.close()
    return result

result = get_unique_words(FILE_PATH)

print(result)
