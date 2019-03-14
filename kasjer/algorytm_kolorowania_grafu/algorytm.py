import queue

def algorytm(grapf, types, start):
    grafQueue = queue.Queue()
    numberOfVertices = len(grapf)
    visited = [0] * numberOfVertices
    gueuedSet = set()

    element = start

    while True:
        visited[element] = 1
        for x in grapf[element]:
            if visited[x] == 0:
                if x not in gueuedSet:
                    grafQueue.put(x)
                    gueuedSet.add(x)
        if 0 not in visited:
            break
        element = grafQueue.get()
    print(visited)

def algorytm2(grapf, types, start):
    grafQueue = queue.Queue()
    numberOfVertices = len(grapf)
    visited = [0] * numberOfVertices

    element = start
    grafQueue.put(element)

    while not grafQueue.empty():
        if visited[element] == 0:
            for x in grapf[element]:
                grafQueue.put(x)
        visited[element] = 1
        element = grafQueue.get()
    print(visited)

def algorytm3(grapf, colors, start):
    grafQueue = queue.Queue()
    numberOfVertices = len(grapf)
    visited = [None] * numberOfVertices

    element = start
    grafQueue.put(element)

    while not grafQueue.empty():
        if visited[element] == None:
            neighboursColors = []
            for x in grapf[element]:
                neighboursColors.append(visited[x])
                grafQueue.put(x)
            for color in colors:
                if color not in neighboursColors:
                    visited[element] = color
                    break
        element = grafQueue.get()
    print(visited)

def createCharTable(n):
    #colors = []
    colors = list()    
    index = ord("a")
    for it in range(index, index + n):
        colors.append(chr(it)) 
    return colors

def createColoredTable(n):
    #colors = []
    colors = list()
    rgb = 0
    tmp = 255//n
    for it in range(n):       
        colors.append([rgb,rgb,rgb])
        rgb +=tmp 
    return colors   

if __name__ == "__main__":
    grafDict = {0: [1, 3, 4], 1: [0, 2, 5, 3], 2: [1, 3, 4, 5], 3: [0, 1, 2, 7, 6], 4: [0, 2, 8, 6], 5: [1, 2, 8, 7, 6], 6: [3, 4, 5, 7], 7: [6, 3, 5, 8], 8: [5, 4, 7]}
    colors = createCharTable(len(grafDict))
    print(colors)
    #algorytm(grafDict, colors, 0)
    print(" ")
    print(" ")
    print(" ")
    algorytm3(grafDict, colors, 0)
