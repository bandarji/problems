from typing import List


Integers = List[int]


TESTS = [
    ([2, 4, 6, 8, 10, 3], 3),
    ([2, 4, 0, 100, 4, 11, 2602, 36], 11),
    ([160, 3, 1719, 19, 11, 13, -21], 160),
]


def find_outlier(integers: Integers) -> int:
    evens, odds = [], []
    for integer in integers:
        if integer & 1:
            odds.append(integer)
        else:
            evens.append(integer)
        if len(odds) > 1 and len(evens) == 1:
            return evens[0]
        if len(evens) > 1 and len(odds) == 1:
            return odds[0]
    return 0


for integers, expected in TESTS:
    response = find_outlier(integers)
    print(f"{integers=} {expected=} {response=}")
    assert find_outlier(integers) == expected
