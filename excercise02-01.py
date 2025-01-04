STRING = "X-DSPAM-Confidence: 0.8475"

result_in_string = STRING.split(':')[1].strip()
result_in_string_1 = STRING[STRING.find(':')+1:STRING.__len__()].strip()

result = float(result_in_string)
result_1 = float(result_in_string_1)

print(result)
print(result_1)