from typing import List


visited = []

def valid(maze, moves):
    i = 1
    j = 1
    for move in moves:
        if move == "W":
            i -= 1

        elif move == "E":
            i += 1

        elif move == "N":
            j -= 1

        elif move == "S":
            j += 1
    if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
        return False
    elif (maze[j][i] == 1):
        return False
    elif (i,j) in visited:
        return False
    visited.append((i,j))
    return True


def findEnd(maze, moves):
    i = 1
    j = 1
    for move in moves:
        if move == "W":
            i -= 1

        elif move == "E":
            i += 1

        elif move == "N":
            j -= 1

        elif move == "S":
            j += 1

    if j == 10 and i == 10:
        #print("Found: " + moves)
        return moves

    return False




def checkio(maze_map: List[List[int]]) -> str:
    # MAIN ALGORITHM
    visited = [(1,1)]
    nums = []
    add = ""
    maze  = maze_map

    while not findEnd(maze, add):
        if nums:
            add = nums.pop(0)
        #print(add)
        for j in ["W", "E", "N", "S"]:
            put = add + j
            if valid(maze, put):
                nums.append(put)

    return add


if __name__ == '__main__':
    print("Example:")
    print(checkio([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]))
