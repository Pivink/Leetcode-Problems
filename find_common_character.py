def commonChars(words):
        
    if len(words) == 1:
        return words[0]

    result = []
    chars = set(words[0])
        
    for char in chars:
        frequency = min([word.count(char) for word in words])
        print(frequency)
        result += frequency * [char]
        print(result)

    return result
print(commonChars(["bella","label","roller"]))
