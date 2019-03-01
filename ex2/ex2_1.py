

def checksum(input):
    file = open(input, "r")
    container_of_letters = {}
    container_general = [0, 0]

    for line in file:
        for c in line:
            if(c in container_of_letters):
                container_of_letters[c] += 1

            else:
                container_of_letters[c] = 1

        prova = container_of_letters.values()
        if (2 in prova):
            container_general[0] += 1
        if (3 in prova):
            container_general[1] += 1

        container_of_letters.clear()

    return container_general[0] * container_general[1]
