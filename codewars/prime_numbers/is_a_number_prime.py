def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for test in range(2, int(number ** 0.5 + 1)):
        if not number % test:
            return False
    return True

tests = (0, 1, 2, 4, 6, 8, 73, 75, -1, 5099)
for test in tests:
    print(test, is_prime(test))
