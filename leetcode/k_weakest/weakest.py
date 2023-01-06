from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        assembled = []
        for index, soldiers in sorted([(i, sum(s)) for i, s in enumerate(mat)], key=lambda t: (t[1], t[0])):
            assembled.append(index)
        return assembled[:k]


solution = Solution()
assert solution.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], 3) == [2, 0, 3]
assert solution.kWeakestRows([[1,0,0,0],[1,1,1,1],[1,0,0,0],[1,0,0,0]], 2) == [0, 2]
