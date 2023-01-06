from typing import List


TESTS = [
    (3, "1 2 Fizz".split()),
    (5, "1 2 Fizz 4 Buzz".split()),
    (15, "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz".split()),
]

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [(
            "FizzBuzz" if not i % (3 * 5)
            else "Fizz" if not i % 3
            else "Buzz" if not i % 5
            else str(i))
            for i in range(1, n + 1)
        ]


solution = Solution()
for number, expected in TESTS:
    assert solution.fizzBuzz(number) == expected
