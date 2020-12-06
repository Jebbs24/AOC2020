from collections import Counter


def count_yes(raw: str) -> int:
    groups = raw.split('\n\n')
    num_yeses = 0
    for group in groups:
        yeses = {char for line in group.split('\n') for char in line.strip()}
        num_yeses += len(yeses)
    return num_yeses


def count_all_yes(raw: str) -> int:
    groups = raw.split('\n\n')
    num_yeses = 0
    for group in groups:
        members = group.split('\n')
        yeses = Counter(char for person in members for char in person)
        num_yeses += sum(count == len(members) for char, count in yeses.items())
    return num_yeses


with open('6.txt') as f:
    answers = f.read()
    print('Part one:', count_yes(answers))
    print('Part two:', count_all_yes(answers))
