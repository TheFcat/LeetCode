from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for i in range(1, n+1):
            graph[i] = {}
        for start, end, time in times:
            graph[start][end] = time

