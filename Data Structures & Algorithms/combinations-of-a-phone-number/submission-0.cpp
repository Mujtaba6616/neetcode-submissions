#include<iostream>
#include<string>
#include<vector>
using namespace std;
class Solution 
{
public:

    unordered_map<char, string> digitToChar = 
    {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
    vector<string> res;
    vector<string> letterCombinations(string digits) 
    {
        if (digits.size()==0){
            return {};
        }
        res.clear();
        backtrack(0,"",digits);
        return res;
    }
    void backtrack(int i , string currState, string digits)
    {
        if (currState.size()==digits.size())
        {
            res.push_back(currState);
            return;
        }
        string letters=digitToChar[digits[i]];
        for (char c: letters)
        {
            backtrack(i+1,currState + c,digits);
        }
    }
};
