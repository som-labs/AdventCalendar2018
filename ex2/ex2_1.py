
def checksum(filename):
    valors_total = {}
    f = open(filename, "r")
# tractem una linia
    for line in f:
        valors = {}
        line2 = line.replace('\n', '')
        for c in line2:
            if c in valors.keys():
                valors[c] += 1
            else:
                valors[c] = 1

        result = {}
        for key, value in valors.items():
            if value not in result.values():
                result[key] = value

# afegim als totals
        for key, value in result.items():
            if value in valors_total.keys():
                valors_total[value] += 1
            else:
                valors_total[value] = 1
    total = 1
    for key, value in valors_total.items():
        if key == 1:
            pass
        else:
            # print("clau: " + str(key) + "  valor: " + str(value))
            total *= value
    return total
