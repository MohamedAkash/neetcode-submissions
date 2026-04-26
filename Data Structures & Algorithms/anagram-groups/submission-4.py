class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time: O(n*klogk) - storing each string of length k, for n strings
        # Space: O(n*k) - storing all strings in the hashmap
        
        hashmap = {}
        
        for s in strs:
            key = "".join(sorted(s))
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(s)
        
        return list(hashmap.values())