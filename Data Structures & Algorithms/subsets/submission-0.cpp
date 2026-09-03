class Solution {
public:
    vector<vector<int>> ans;
    vector<int> subset;
    void backtrack(int i,vector<int>& nums){
        if (i>=nums.size()){
            ans.emplace_back(subset);
            return;
        }
        subset.push_back(nums[i]);
        backtrack(i+1,nums);
        subset.pop_back();
        backtrack(i+1,nums);

    }
    vector<vector<int>> subsets(vector<int>& nums) {
        if (nums.size()==0){
            ans.push_back({});
            return ans;
        }
        backtrack(0,nums);
        return ans;
    }
};
