#include <algorithm>
#include <iostream>
#include <vector>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) 
    {   
        vector<int> res;
        vector<int> temp=nums;
        vector<int> ans;
        sort(nums.begin(),nums.end());
        int i=0;
        int j=nums.size()-1;
        while (i<j)
        {
            if (nums[i]+nums[j]<target){
                i++;
            }
            else if (nums[i]+nums[j]>target){
                j--;
            }
            else{
                res.push_back(nums[i]);
                res.push_back(nums[j]);
                break;
            }
        }
        int a=res[0];
        int b=res[1];
        for (int i=0;i<temp.size();i++)
        {
            if (temp[i]==a){
                ans.push_back(i);
            }
            else if (temp[i]==b){
                ans.push_back(i);
            }
        }
        return ans;

    }

};
