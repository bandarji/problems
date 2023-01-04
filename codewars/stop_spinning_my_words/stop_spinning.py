TESTS = [
    ("Hey fellow warriors", "Hey wollef sroirraw"),
    ("This is a test", "This is a test"),
    ("This is another test", "This is rehtona test"),
]

def spin_words(sentence: str) -> str:
    return " ".join(w if len(w) < 5 else w[::-1] for w in sentence.split())

for test, expected in TESTS:
    response = spin_words(test)
    print(f"{test=}, {expected=}, {response=}")
    assert response == expected
