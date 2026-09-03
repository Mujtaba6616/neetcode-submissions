from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        
        for word in strs:
            key = ''.join(sorted(word))

            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)

        list_of_lists = list(hashmap.values())

        return list_of_lists
