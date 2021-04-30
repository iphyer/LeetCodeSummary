class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect.bisect_left(nums, target)
        r = bisect.bisect_right(nums, target)
        
        if l <= (r-1):
            return [l,r-1]
        else:
            return [-1,-1]
