def unique_in_order(sequence):
    if not sequence or not isinstance(sequence, (str, list, tuple, dict)):
        return []
    response = [sequence[0]]
    for element in sequence[1:]:
        if element == response[-1]:
            continue
        response.append(element)
    return response


tests = [
    "AAAABBBCCDAABBB",
    "ABBCcAD",
    [1,2,2,3,3],
]

for test in tests:
    print(test, unique_in_order(test))
