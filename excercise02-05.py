FILE_PATH = "mbox-short.txt"
KEY = "From "

def count_messages_by_hour(file_path) -> dict:
    file = open(file_path, 'r')
    result = {}

    for line in file:
        if not line.startswith(KEY):
           continue
        else:
            words = line.split(":")
            hour = words[0][-2:]
            if hour not in result:
                result[hour] = 1
            else:
                result[hour] += 1
    file.close()                    
    return result
            
result = sorted(count_messages_by_hour(FILE_PATH).items())       
print(result)