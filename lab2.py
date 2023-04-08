def dictionary1(words):
    dic = {}
    for word in words:
        if word in dic:
            dic[word] = dic[word] + 1
        else:
            dic[word] = 1
    return dic
words = input().split()
dictionary = dictionary1(words)
keys = sorted(dictionary.keys())
for key in keys:
    print(key + ': ' + str(dictionary[key]))