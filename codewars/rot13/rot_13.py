TESTS = [
    ("test", "grfg"),
    ("Test", "Grfg"),
    ("aA bB zZ 1234 *!?%", "nN oO mM 1234 *!?%"),
]

# def rot131(message: str) -> str:
#     alpha_lower = "abcdefghijklmnopqrstuvwxyz"
#     alpha_upper = alpha_lower.upper()
#     response = []
#     for char in message:
#         if char in alpha_lower:
#             response.append(alpha_lower[(alpha_lower.index(char) + 13) % 26])
#         elif char in alpha_upper:
#             response.append(alpha_upper[(alpha_upper.index(char) + 13) % 26])
#         else:
#             response.append(char)
#     return "".join(response)

def rot13(message: str) -> str:
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = alpha_lower.upper()
    return "".join(
            alpha_lower[(alpha_lower.index(char) + 13) % 26] if char in alpha_lower
            else alpha_upper[(alpha_upper.index(char) + 13) % 26] if char in alpha_upper
            else char
            for char in message
        )


for test, expected in TESTS:
    assert rot13(test) == expected
