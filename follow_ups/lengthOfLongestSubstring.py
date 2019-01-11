# Note: 
    # can not init maxlength == 1: 
    # corner case: s = ""
# Note 2: 
    # update start pointer : 
        # start = usedChar[s[i]] + 1
# note 3:
    # need to make sure the start update only when:  and start <= usedChar[s[i]]:
    
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
                
            usedChar[s[i]] = i
        
        return maxLength          
