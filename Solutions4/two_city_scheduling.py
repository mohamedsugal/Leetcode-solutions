from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total_cost = 0
        costs.sort(key=lambda x: x[0] - x[1])
        for i in range(len(costs)):
            if i < len(costs) // 2:
                total_cost += costs[i][0]
            else:
                total_cost += costs[i][1]
        return total_cost


costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
s = Solution()
print(s.twoCitySchedCost(costs))
