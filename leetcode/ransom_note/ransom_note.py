TESTS = [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
]

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq_magazine = {}
        for char in magazine:
            freq_magazine[char] = freq_magazine.get(char, 0) + 1
        for char in ransomNote:
            freq_magazine[char] = freq_magazine.get(char, 0) - 1
            if freq_magazine[char] < 0:
                return False
        return True


solution = Solution()
for note, magazine, expected in TESTS:
    assert solution.canConstruct(note, magazine) == expected
