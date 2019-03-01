

# Prova 2
def ex1_2(input):
    f = open(input, "r")
    acum = 0
    generats = set()
    generats.add(acum)
    trobat = False

    while not trobat:
        for num in f:
            acum += int(num)
            if (acum not in generats):
                generats.add(acum)
            else:
                trobat = True
                break
        else:
            if (not trobat):
                f.close()
                f = open(input, "r")
    return acum
