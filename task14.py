sentence = input("Input sentence:  ")

result = sentence.index('f')
result_revetse = len(sentence) - 1 - sentence[::-1].index('f') 
print(result)

print(result_revetse)
