class Solution:
    def firstOcc(self, nums, target):
        first = -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high)// 2
            if nums[mid] == target:
                first = mid
                high = mid - 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid -1
        return first

    def lastOcc(self, nums, target):
        last = -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high)// 2

            if nums[mid] == target:
                last = mid
                low = mid + 1
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid -1
        return last
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.firstOcc(nums,target)
        if first == -1:
            return [-1,-1]
        last = self.lastOcc(nums, target)

        return [first,last]       