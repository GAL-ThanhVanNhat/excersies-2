FILE_PATH = "mbox-short.txt"
KEY = "Author"

def count_messages(file_path) -> dict:
    file = open(file_path, 'r')
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
    file.close()
    return result

result = count_messages(FILE_PATH)
           
print(result)