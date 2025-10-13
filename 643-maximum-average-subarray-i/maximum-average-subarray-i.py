class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowSum = maxSum = sum(nums[:k])

        for i in range(k,len(nums)):
            windowSum += nums[i] - nums[i-k]
            maxSum = max(maxSum,windowSum)

        return maxSum/k