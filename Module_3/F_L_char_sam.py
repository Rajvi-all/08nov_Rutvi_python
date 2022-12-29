def match_word(words):
    ctr = 0

    for word in words:
        if len (word) > 1 and word [0] == word[-1]:
            ctr += 1
    return ctr
print(match_word(['abc','xyz','aba','1221']))            