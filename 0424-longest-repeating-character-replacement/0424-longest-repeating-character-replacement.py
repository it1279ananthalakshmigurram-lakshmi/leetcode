class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        left=0
        longest=0
        max_count=0
        for right in range(len(s)):
            d[s[right]]=d.get(s[right],0)+1
            max_count=max(max_count,d[s[right]])
            while(right-left+1)-max_count>k:
                d[s[left]]-=1
                left=left+1
            longest=max(longest,right-left+1)
        return longest