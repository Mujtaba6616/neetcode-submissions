#include<iostream>
#include<vector>
#include<queue>
using namespace std;
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) 
    {
        unordered_map<int,int> hashmap;
        vector<int> ans;
        for (int i=0;i<nums.size();i++)
        {
            hashmap[nums[i]]++;
        }
        priority_queue <pair<int,int>> maxHeap;
        for (auto &it: hashmap)
        {
            maxHeap.push({it.second,it.first});
        }
        for (int i=0;i<k;i++)
        {
            ans.push_back(maxHeap.top().second);
            maxHeap.pop();
        }
        return ans;
    }
};
