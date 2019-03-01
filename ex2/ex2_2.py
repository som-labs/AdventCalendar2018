

def common_letters(input):
    file = open(input, "r")
    container_of_words = []
    common_chars = []
    for line in file:
        line2 = line.replace('\n', '')
        container_of_words.append(line2)

    for word1 in container_of_words:
        aux = container_of_words[:]
        aux.remove(word1)
        for word2 in aux:
            common = sum(1 if c1 == c2 else 0 for c1, c2 in zip(word1, word2))
            if (common) == (len(word1) - 1):
                for c1, c2 in zip(word1, word2):
                    if c1 == c2:
                        common_chars.append(c1)
                common_chars = ''.join(str(e) for e in common_chars)
                return common_chars

    return "ERROR"


# resultat = common_letters("inputs/inputMarta1.txt")
# print(resultat)
