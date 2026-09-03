class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset=set()
        for i in range(len(nums)):
            hashset.add(nums[i])
        a=[]
        for i in hashset:
            if i-1 not in hashset:
                a.append(i)
        inc=1
        length=1
        longest=1
        if len(hashset)==0:
                return 0
        for i in range(len(a)):
            while a[i]+inc in hashset:
                length+=1
                inc+=1
            if longest<length:
                longest=length
            length=1
            inc=1
        return longest

                


                 
