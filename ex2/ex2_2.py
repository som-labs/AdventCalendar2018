
def findTwice(filename):
    valors = []
    valors_set = set()
    f = open(filename, "r")
    for line in f:
        line2 = line.replace('\n', '')
        valors.append(line2)
    longitud = len(valors[0])

    for i in range(0, longitud):
        valors_set.clear()
        for entrada in valors:
            str1 = entrada[0:i] + entrada[i + 1:longitud]
            if str1 not in valors_set:
                valors_set.add(str1)
            else:
                return str1
