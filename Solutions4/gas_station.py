from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus, dificit = 0, 0
        station = 0

        for i, liters in enumerate(gas):
            surplus += liters - cost[i]
            dificit += liters - cost[i]
            if dificit < 0:
                station = i + 1
                dificit = 0

        return station if surplus >= 0 else -1


# gas = [1, 2, 3, 4, 5]
# cost = [3, 4, 5, 1, 2]
# gas = [5, 1, 2, 3, 4]
# cost = [4, 4, 1, 5, 1]
gas = [3, 1, 1]
cost = [1, 2, 2]
s = Solution()
print(s.canCompleteCircuit(gas, cost))
