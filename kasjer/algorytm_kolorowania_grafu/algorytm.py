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


types = ["a", "b", "c", "d", "e", "f", "g", "h"]
grafDict = {0: [1, 3, 4], 1: [0, 2, 5, 3], 2: [1, 3, 4, 5], 3: [0, 1, 2, 7, 6], 4: [0, 2, 8, 6], 5: [1, 2, 8, 7, 6], 6: [3, 4, 5, 7], 7: [6, 3, 5, 8], 8: [5, 4, 7]}
algorytm(grafDict, types, 0)
print(" ")
print(" ")
print(" ")
algorytm2(grafDict, types, 0)
