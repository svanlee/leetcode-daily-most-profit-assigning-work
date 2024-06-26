from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        i, res = 0, 0
        best = 0
        for w in sorted(worker):
            while i < len(jobs) and jobs[i][0] <= w:
                best = max(best, jobs[i][1])
                i += 1
            res += best
        return res       