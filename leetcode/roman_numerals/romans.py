TESTS = [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
]

class Solution:
    def romanToInt(self, s: str) -> int:
        total, cursor = 0, 0
        mappings = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        distance = len(s)
        while cursor < distance:
            if cursor + 1 < distance and s[cursor : cursor + 2] in mappings:
                total += mappings[s[cursor : cursor + 2]]
                cursor += 1
            else:
                total += mappings[s[cursor]]
            cursor += 1
        return total

solution = Solution()
for roman_numeral, expected_integer in TESTS:
    assert solution.romanToInt(roman_numeral)
