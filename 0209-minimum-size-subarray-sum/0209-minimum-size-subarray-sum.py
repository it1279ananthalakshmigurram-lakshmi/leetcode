class Solution:
    def minSubArrayLen(self, target: int, arr: List[int]) -> int:
        left=0
        curr_sum=0
        min_len=float('inf')#->infinity
        for right in range(len(arr)):
            curr_sum=curr_sum+arr[right]
            while curr_sum>=target:
                min_len=min(min_len,right-left+1)
                curr_sum=curr_sum-arr[left]
                left=left+1
        if min_len==float('inf'):
            return 0
        return min_len
       