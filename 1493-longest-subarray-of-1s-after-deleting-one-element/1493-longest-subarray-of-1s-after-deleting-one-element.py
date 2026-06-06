class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left=0
        zero=0
        res=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero=zero+1
            while(zero>1):
                if nums[left]==0:
                    zero=zero-1
                left=left+1
            res=max(res,right-left)
        return res



        