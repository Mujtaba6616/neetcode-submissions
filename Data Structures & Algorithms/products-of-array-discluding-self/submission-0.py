class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        var = 1
        var1 = 1
        pro = []
        pre = []
        ans = [0] * len(nums)

        for i in range(len(nums)):
            var *= nums[i]
            pro.append(var)

        for i in range(len(nums)-1, -1, -1):
            var1 *= nums[i]
            pre.append(var1)
        pre = pre[::-1]

        for i in range(len(nums)):
            if i - 1 >= 0 and i + 1 <= len(nums) - 1:
                ans[i] = pro[i-1] * pre[i+1]
            elif i - 1 >= 0 and i + 1 > len(nums) - 1:
                ans[i] = pro[i-1]
            elif i - 1 < 0 and i + 1 <= len(nums) - 1:
                ans[i] = pre[i+1]
            else:
                ans[i] = 1

        return ans
