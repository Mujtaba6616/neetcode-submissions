class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic={}
        st=s.split()
        if len(st)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dic and st[i] not in dic.values():
                dic[pattern[i]]=st[i]
        print(dic)
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                return False
            if dic[pattern[i]] != st[i]:
                return False
        return True
