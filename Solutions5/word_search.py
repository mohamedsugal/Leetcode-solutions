from typing import List, Dict


# Given a list of words and an M x N board of characters,
# find all possible words in the list that can be formed
# by a sequence of adjacent characters on the board.
def find_adjacent(board: List[List[str]], i: int, j: int) -> List[str]:
    adjacent = []
    rows, columns = len(board), len(board[0])
    for r in [-1, 0, 1]:
        for c in [-1, 0, 1]:
            if r == c == 0:
                continue
            if 0 <= i + r < rows and 0 <= j + c < columns:
                adjacent.append(board[i + r][j + c])
    return adjacent


def construct_graph(board: List[List[str]]) -> Dict[str, List[str]]:
    graph = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            curr = board[i][j]
            if curr not in graph:
                graph[curr] = find_adjacent(board, i, j)
    return graph


# TODO: Do DFS or BFS to check if there exists a bath
def word_exists(graph: Dict[str, List[str]], word: List[str]) -> bool:
    visited = set()
    queue = []
    if word not in graph.keys():


words = ["GUEST", "FOR", "ARE", "QUIT"]
board = [['G', 'I', 'Z'],
         ['A', 'U', 'T'],
         ['Q', 'S', 'E']]
# Output: "GUEST", "QUIT"

print(find_adjacent(board, 1, 1))
# print(construct_graph(board))
