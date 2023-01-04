TESTS = [
    (16, 7),
    (942, 6),
    (132189, 6),
    (493193, 2),
]


def digital_root(number: int) -> int:
    while number > 9:
        number = sum(int(d) for d in str(number))
    return number


for number, expected in TESTS:
    assert digital_root(number) == expected
