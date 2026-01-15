# problem link https://leetcode.com/problems/valid-anagram/

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
        if len(s) != len(t):
            return False
        
        # Count frequency of each character in both strings
        count_s = Counter(s)
        count_t = Counter(t)
        
        # Compare the two counters
        return count_s == count_t
