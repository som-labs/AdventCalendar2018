
def ex1_1(input):
    f = open(input, "r")
    acum = 0
    for x in f:
        acum += int(x)
    return acum

