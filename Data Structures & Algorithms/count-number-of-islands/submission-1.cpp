#include<iostream>
#include<set>
#include<vector>
#include<deque>
using namespace std;
class Solution {
public:
    set <pair<int,int>> visited;
    void bfs(int r,int c,int rows,int cols,vector<vector<char>>& grid)
        {
            deque<pair<int,int>> q;
            visited.insert({r,c});
            q.push_back({r,c});
            vector <pair<int,int>> directions={
                {1,0},
                {-1,0},
                {0,1},
                {0,-1}
            };
            while (!q.empty())
            {
                auto current=q.front();
                q.pop_front();
                int i=current.first;
                int j=current.second;
                for (auto dir: directions)
                {
                    int dr=dir.first;
                    int dc=dir.second; 
                    int nr=i+dr;
                    int nc=j+dc;
                    if (nr>=0 && nr<rows && nc>=0 && nc<cols && grid[nr][nc]=='1' && !visited.count({nr,nc}))
                    {
                        q.push_back({nr,nc});
                        visited.insert({nr,nc});
                    }
                }
                    

            }
        }
   
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty() || grid[0].empty()){
            return 0;
        }
        int row=grid.size();
        int col=grid[0].size();
        
        int islands=0;
        
        for (int r=0;r<row;r++) {
            for (int c=0;c<col;c++) {
                if(grid[r][c]=='1' && !visited.count({r,c}))
                {
                    bfs(r,c,row,col,grid);
                    islands++;
                }
            }
        }
        return islands;
    }
};
