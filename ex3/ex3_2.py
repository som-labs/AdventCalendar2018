

def get_box(input):
    file = open(input, "r")
    m = set()
    solapats = set()
    id_no_solapats = set()
    id_solapats = set()
    auxiliar = set()
    for line in file:
        aux = line.replace(" ", "").replace("#", "")
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
                    solapats.add(str(posicio))
                    if id in id_no_solapats:
                        id_no_solapats.remove(id)
                    id_solapats.add(id)
                else:
                    m.add(posicio)
                    if id not in id_solapats:
                        id_no_solapats.add(id)
                    auxiliar.add(id + ":" + str(posicio))
    for s in auxiliar:
        n, p = s.split(":")
        if p in solapats:
            if n in id_no_solapats:
                id_no_solapats.remove(n)
    for id in id_no_solapats:
        return id
