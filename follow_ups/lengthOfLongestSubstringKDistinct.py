# MEthod using counting 

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = 0
        maxLength = 0
        disChar = {}
        
        for i in range(len(s)):
            if s[i] in disChar: 
                disChar[s[i]] += 1
            else: 
                disChar[s[i]] = 1
                if len(disChar) > k:
                    while (len(disChar) > k):
                        disChar[s[start]] -= 1
                        if disChar[s[start]] == 0:
                            del disChar[s[start]]
                        start += 1
                            
            maxLength = max(maxLength, i - start + 1)
            
        return maxLength
