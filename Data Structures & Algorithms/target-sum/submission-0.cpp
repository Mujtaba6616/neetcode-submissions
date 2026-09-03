class Solution {
public:
    int ans = 0;

    void backtrack(int i, int sum, vector<int>& nums, int target)
    {
        if (i == nums.size())
        {
            if (sum == target)
                ans++;
            return;
        }

        backtrack(i + 1, sum + nums[i], nums, target);
        backtrack(i + 1, sum - nums[i], nums, target);
    }

    int findTargetSumWays(vector<int>& nums, int target)
    {
        backtrack(0, 0, nums, target);
        return ans;
    }
};