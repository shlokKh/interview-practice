#https://www.chegg.com/homework-help/questions-and-answers/task-davy-buried-pieces-ancient-artifacts-underground-artifacts-hidden-area-split-nxn-grid-q51996391
from typing import List
from collections import defaultdict

def solution(n: int, artifacts: str, searched: str) -> List[int]:
    size = {} #mapping of artificats and their respective sizes
    current = defaultdict(lambda: 0) #mapping of currently searched artifacts
    grid = [[0]*n for _ in range(n)] # this is the grid where artificats will be found max: 26x26
    artifactId = 1
    complete = 0
    pieces = 0
    def findHidden(beginning: str, ending: str, id: int):
        topLeft = min(beginning, ending)
        bottomRight = max(beginning, ending)
        
        topLeft = (int(topLeft[0])-1, ord(topLeft[1]) - 65)
        bottomRight = (int(bottomRight[0])-1, ord(bottomRight[1]) - 65)

        if topLeft[0] != bottomRight[0] and topLeft[1] != bottomRight[1]:
            bottomLeft = (topLeft[0] + 1, topLeft[1])
            topRight = (bottomRight[0] - 1, bottomRight[1])
            grid[topLeft[0]][topLeft[1]] = id
            grid[topRight[0]][topRight[1]] = id
            grid[bottomLeft[0]][bottomLeft[1]] = id
            grid[bottomRight[0]][bottomRight[1]] = id
            size[id] = 4
        elif topLeft == bottomRight:
            grid[topLeft[0]][topLeft[1]] = id
            size[id] = 1
        elif topLeft[0] != bottomRight[0]:
            grid[topLeft[0]][topLeft[1]] = id
            grid[bottomRight[0]][bottomRight[1]] = id
            size[id] = 2
            curr = topLeft[0]+1
            while curr != bottomRight[0]:
                grid[curr][topLeft[1]] = id
                size[id] += 1
                curr += 1
        elif topLeft[1] != bottomRight[1]:
            grid[topLeft[0]][topLeft[1]] = id
            grid[bottomRight[0]][bottomRight[1]] = id
            size[id] = 2
            curr = topLeft[1] + 1
            while curr != bottomRight[1]:
                grid[topLeft[0]][curr] = id
                size[id] += 1
                curr += 1
    for artifact in artifacts.split(', '):
        positions = artifact.split()

        findHidden(positions[0], positions[1], artifactId)
        artifactId += 1        

    for search in searched.split(' '):
        pos = (int(search[0])-1, ord(search[1])-65)
        currArtifact = grid[pos[0]][pos[1]]
        if currArtifact != 0:
            current[currArtifact] += 1
            grid[pos[0]][pos[0]] = 0
            if current[currArtifact] == size[currArtifact]:
                complete += 1
                pieces -= size[currArtifact]
                del current[currArtifact]
            pieces += 1
    print(grid)
    print(size)
    return [complete, pieces]
            
print(solution(4, '1B 2C, 2D 4D', '2B 2D 3D 4D 4A'))

#probz won't work
# def solutionFail(n: int, artifacts: str, searched: str) -> List[int]:
#     locations = {}
#     size = {}
#     numArtificats = 1
#     def findHidden(beginning: str, ending: str, id: int):
#         topLeft = min(beginning, ending)
#         bottomRight = max(beginning, ending)

#         if topLeft[0] != bottomRight[0] and topLeft[1] != bottomRight[1]:
#             bottomLeft = str(int(topLeft[0])+1) + topLeft[1]
#             topRight = str(int(bottomRight[0])-1) + bottomRight[1]
#             locations[id] = {topLeft, topRight, bottomLeft, bottomRight}
#         elif topLeft[0] != bottomRight[0]:
#             locations[id] = {topLeft, bottomRight}
#             curr = str(int(topLeft[0])+1) + topLeft[1]
#             while curr != bottomRight:
#                 locations[id].add(curr)
#                 curr = str(int(curr[0])+1) + curr[1] 
#         else:
#             locations[id] = {topLeft, bottomRight}
#             curr = topLeft[0] + chr(ord(topLeft[1])+1)
#             while curr != bottomRight:
#                 locations[id].add(curr)
#                 curr = curr[0] + chr(ord(curr[1])+1)
        
#         size[id] = len(locations[id])

#     for artifact in artifacts.split(', '):
#         positions = artifact.split()
#         findHidden(positions[0], positions[1], numArtificats)
#         numArtificats += 1
