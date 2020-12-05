from typing import NamedTuple


class Seat(NamedTuple):
    column: int
    row: int
    @property
    def seat_id(self) -> int:
        return self.row * 8 + self.column


def find_seat(boarding_pass: str) -> Seat:
    row = 0
    column = 0
    for i, c in enumerate(boarding_pass[:7]):
        multipler = 2 ** (6 - i)
        include = 1 if c == 'B' else 0
        row += multipler * include
    for i, c in enumerate(boarding_pass[-3:]):
        multipler = 2 ** (2 - i)
        include = 1 if c == 'R' else 0
        column += multipler * include
    return Seat(column, row)


def find_my_seat(seats: list) -> int:
    seat_ids = [seat.seat_id for seat in seats]
    lo = min(seat_ids)
    hi = max(seat_ids)
    my_seat = [x for x in range(lo, hi) if x not in seat_ids]
    return my_seat[0]


with open('5.txt') as f:
    seats = [find_seat(boarding_pass.strip()) for boarding_pass in f]
    print("Part one:", max([seat.seat_id for seat in seats]))
    print("Part two:", find_my_seat(seats))
