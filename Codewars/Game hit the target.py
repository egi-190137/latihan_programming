def solution(mtrx):
    for array in mtrx:
        if '>' in array:
            if 'x' not in array or array.index('>') > array.index('x'):
                return False
            else:
                return True


matrix = [
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', '>', ' ', 'x'],
  [' ', ' ', '', ' ', ' ']
]

print(solution(matrix))