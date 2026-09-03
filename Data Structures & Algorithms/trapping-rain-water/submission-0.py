class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        ans1=0
        max_l=[0]*len(height)
        max_r=[0]*len(height)
        for i in range(len(height)):
            if(i-1<0):
                max_l[i]=0
            else:
                max_l[i]=max(max_l[i-1],height[i-1])
        j=len(height)-1
        while(j>=0):
            if(j+1>len(height)-1):
                max_r[j]=0
            else:
                max_r[j]=max(max_r[j+1],height[j+1])
            j=j-1

        for i in range(1,len(height)-1):
            ans1=min(max_l[i],max_r[i])-height[i]
            if(ans1<0):
                ans1=0
            ans=ans+ans1

        return ans
        