slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
ans = 1
tree_map = []
for line in open('3.txt').read().splitlines():
    tree_map.append(list(line.strip()))

for (x, y) in slopes:
    row = 0
    column = 0
    score = 0
    while row < len(tree_map):
        row += y
        column += x
        if row < len(tree_map) and tree_map[row][column % len(tree_map[row])] == '#':
            score += 1
    ans *= score
    if x == 3 and y == 1:
        print('Part one: ', score)
print('Part two: ', ans)
