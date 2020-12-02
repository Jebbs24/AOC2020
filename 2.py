lines = [i for i in open('2.txt').read().splitlines()]


def part_one():
    count = 0
    for i in lines:
        low_req = int(i.split()[0].split('-')[0])
        high_req = int(i.split()[0].split('-')[1])
        key = i.split()[1].strip(':')
        passwd = i.split()[2]
        key_count = passwd.count(key)
        if low_req <= key_count <= high_req:
            count = count + 1

    print("Part one: ", count)


def part_two():
    count = 0
    for i in lines:
        low_req_space = int(i.split()[0].split('-')[0]) - 1
        high_req_space = int(i.split()[0].split('-')[1]) - 1
        key = i.split()[1].strip(':')
        passwd = i.split()[2]
        try:
            if passwd[low_req_space] == passwd[high_req_space]:
                continue
            elif key == passwd[low_req_space]:
                count = count + 1
            elif key == passwd[high_req_space]:
                count = count + 1
            else:
                continue
        except IndexError:
            continue

    print("Part Two: ", count)


part_one()
part_two()
