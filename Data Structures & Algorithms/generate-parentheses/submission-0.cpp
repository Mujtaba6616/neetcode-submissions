class Solution {
public:
    vector<string> ans;
    int open=0;
    int close=0;
    string subset="";
    void backtrack(int n)
    {
        if (open == n && close == n)
        {
            ans.emplace_back(subset);
            return;
        }
        if (open<n){
            subset.push_back('(');
            open+=1;
            backtrack(n);
            open--;
            subset.pop_back();

        }
        if (close<open){
            subset.push_back(')');
            close+=1;
            backtrack(n);
            close--;
            subset.pop_back();

        }
        
    }
    vector<string> generateParenthesis(int n) 
    {
        if (n==0){
            ans.push_back(subset);
            return ans;
        }
        backtrack(n);   
        return ans;
    }
};
