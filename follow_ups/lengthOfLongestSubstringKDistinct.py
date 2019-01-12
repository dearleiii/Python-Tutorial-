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

    # SOL 2: using index 
        def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k:
                low = min(d.values())
                del d[s[low]]
                low += 1
            ret = max(i - low + 1, ret)
        return ret
