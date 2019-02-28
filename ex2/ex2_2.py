
def findTwice(filename):
    valors = []
    f = open(filename, "r")
    for line in f:
        line2 = line.replace('\n', '')
        valors.append(line2)
# tractem 
    for i in range(0, 5):
        substrings = {}
        for x in valors:
            str1 = x[0:i] + x[i:5]
            

findTwice("input/inputDavid2.txt")
