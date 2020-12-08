from typing import NamedTuple, Dict, List, Tuple
import re
from collections import defaultdict

RAW = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


class Bag(NamedTuple):
    color: str
    contains: Dict[str, int]


def parse_input(line: str) -> Bag:
    part1, part2 = line.split(" contain ")
    color = part1[:-5]
    part2 = part2.rstrip(".")
    if part2 == "no other bags":
        return Bag(color, {})
    contains = {}
    contained = part2.split(", ")
    for sub_bag in contained:
        sub_bag = re.sub(r"bags?$", "", sub_bag)
        first_space = sub_bag.find(" ")
        count = int(sub_bag[:first_space].strip())
        color2 = sub_bag[first_space:].strip()
        contains[color2] = count
    return Bag(color, contains)


def make_bags(data: str) -> List[Bag]:
    return [parse_input(line) for line in data.split("\n")]


def parents(bags: List[Bag]) -> Dict[str, List[str]]:
    ic = defaultdict(list)
    for bag in bags:
        for child in bag.contains:
            ic[child].append(bag.color)
    return ic


def can_eventually_contain(bags: List[Bag], color: str) -> List[str]:
    parent_map = parents(bags)
    check_me = [color]
    can_contain = set()
    while check_me:
        child = check_me.pop()
        for parent in parent_map.get(child, []):
            if parent not in can_contain:
                can_contain.add(parent)
                check_me.append(parent)

    return list(can_contain)


def num_bags_inside(bags: List[Bag], color: str) -> int:
    by_color = {bag.color: bag for bag in bags}
    num_bags = 0
    stack: List[Tuple[str, int]] = [(color, 1)]
    while stack:
        next_color, multiplier = stack.pop()
        bag = by_color[next_color]
        for child, count in bag.contains.items():
            num_bags += multiplier * count
            stack.append((child, count * multiplier))
    return num_bags


with open('7.txt') as f:
    raw = f.read()
    bags_list = make_bags(raw)
    print("Part one:", len(can_eventually_contain(bags_list, 'shiny gold')))
    print("Part:2", num_bags_inside(bags_list, "shiny gold"))
