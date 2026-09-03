class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []                     # CHANGE 1
        ans = [0] * len(temperatures)  # CHANGE 2

        for i in range(len(temperatures)):
            # CHANGE 3
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_index = stack.pop()          # CHANGE 4
                ans[prev_index] = i - prev_index  # CHANGE 5

            stack.append(i)  # CHANGE 6

        return ans
