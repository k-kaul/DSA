class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        i,j=0,k-1

        minDiff = 100000

        while j<len(nums):
            minDiff = min(minDiff, nums[j] - nums[i])
            i+=1
            j+=1
        return minDiff
