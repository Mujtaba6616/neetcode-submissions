class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        paired_list = list(zip(position, speed))
        paired_list.sort(reverse=True)  # Closest to target first
        
        stack = []
        
        # Iterate from farthest car to closest
        for position, speed in paired_list:
            temp = (target - position) / speed
            stack.append(temp)
            
            # Merge with fleet ahead if needed
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # ✅ must call pop()
        
        return len(stack)
