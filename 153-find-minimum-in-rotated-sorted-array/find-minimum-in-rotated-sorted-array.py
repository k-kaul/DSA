class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        minNum = float('inf')
        while low <= high:
            mid = (low + high)// 2
            
            if nums[low] <= nums[mid]:
                minNum = min(nums[low], minNum)
                low = mid + 1
            else:
                high = mid - 1
                minNum = min(nums[mid], minNum)
        return minNum        