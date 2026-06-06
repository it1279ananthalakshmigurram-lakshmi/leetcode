class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target=sum(nums)-x
        if target==0:
            return len(nums)
        if target<0:
            return -1
        left=0
        curr_sum=0
        longest=-1
        for right in range(len(nums)):
            curr_sum=curr_sum+nums[right]
            while curr_sum>target:
                curr_sum=curr_sum-nums[left]
                left+=1
            if curr_sum==target:
                longest=max(longest,(right-left+1))
        if longest==-1:
            return -1
        return len(nums)-longest
        