def Replace_words(dictionary, sentence):
    dictionary.sort(key=len)
    words = sentence.split()  
    for i in range(len(words)):
        for prefix in dictionary:
            if words[i].startswith(prefix):
                words[i] = prefix
                break

    return " ".join(words)

d = ["catt", "cat", "bat", "rat"]
s = "the cattle was rattled by the battery"
print(Replace_words(d, s))