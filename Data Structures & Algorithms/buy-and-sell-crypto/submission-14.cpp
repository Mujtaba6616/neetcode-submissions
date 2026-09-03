#include<iostream>
#include<vector>
#include<climits>
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i=0;
        int j=1;
        int maxProfit=INT_MIN;
        while (j<prices.size())
        {
            if (prices[i]>prices[j]){
                i=j;
                j++;
            }
            else if (prices[i]<=prices[j]){
                if (prices[j]-prices[i]>maxProfit)
                {
                    maxProfit=prices[j]-prices[i];
                    cout<<maxProfit;
                }
                j++;
            }
        }
        if (maxProfit==INT_MIN){
            return 0;
        }
        return maxProfit;
    }
};
