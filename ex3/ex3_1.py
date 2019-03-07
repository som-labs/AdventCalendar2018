

def get_boxes_overlaped(input):
    file = open(input, "r")
    m = set()
    solapats = set()
    for line in file:
        aux = line.replace(" ", "")
        aux = aux.replace("#", "")
        id, rest = aux.split("@")
        x, rest = rest.split(",")
        y, rest = rest.split(":")
        px, py = rest.split("x")

        x = int(x)
        y = int(y)
        posx = int(px)
        posy = int(py)

        for i in range(0, posx):  # Consultem X
            for j in range(0, posy):  # Consultem Y
                posicio = ((x + i), (y + j))
                if posicio in m:
                    solapats.add(posicio)
                else:
                    m.add(posicio)

    return len(solapats)
