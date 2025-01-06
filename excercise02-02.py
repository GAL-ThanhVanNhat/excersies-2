KEY = "X-DSPAM-Confidence:"
FILE_PATH = "mbox.txt"

def get_average_confidence(file_path) -> float:
    file =  open(file_path, 'r')
    confidence_array = []

    for line in file:
        if not line.startswith(KEY):
            continue
        else:
            confidence = float(line.split(':')[1].strip())
            confidence_array.append(confidence)
        
    result = sum(confidence_array)/len(confidence_array)
    file.close()
    return result
    
result = get_average_confidence(FILE_PATH)
print(result)