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


def check_word(graph: Dict[str, List[str]], word: str) -> bool:
    if not word:
        return False
    visited = set()
    if word[0] not in graph.keys():
        return False
    queue, i = [word[0]], 0
    visited.add(word[0])
    while queue:
        curr_char = queue.pop()
        if word[len(word) - 1] == curr_char:
            return True
        i += 1
        next_char = word[i]
        if next_char in graph[curr_char]:
            queue.append(next_char)
            visited.add(next_char)
    return False


def word_exists(board: List[List[str]], words: List[str]) -> List[str]:
    result = []
    graph = construct_graph(board)
    for word in words:
        if check_word(graph, word):
            result.append(word)
    return result


test_words = ["GUEST", "FOR", "ARE", "QUIT"]
test_words2 = []
test_words3 = ["QUIZ", "ZEBRA", "GUT", ""]
test_board = [['G', 'I', 'Z'],
              ['A', 'U', 'T'],
              ['Q', 'S', 'E']]
# Output: "GUEST", "QUIT"
print(word_exists(test_board, test_words2))
