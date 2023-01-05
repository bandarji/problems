TESTS = [
    (1, "*\n"),
    (2, None),
    (3, " *\n***\n *\n")

]


def diamond(n: int) -> str | None:
    if n < 1 or not n & 1:
        return None
    pattern = []
    step = 0
    end = "\n" if n > 1 else ""
    while n >= 1:
        pattern.append(f"{' ' * step}{'*' * n}")
        n -= 2
        step += 1
    return "\n".join(pattern[::-1]) + "\n" + "\n".join(pattern[1:]) + end


for test, expected in TESTS:
    response = diamond(test)
    print(f"{test=} {expected=} {response=}")
