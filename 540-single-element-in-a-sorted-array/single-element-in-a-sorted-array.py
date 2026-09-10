class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        arrLen = len(nums)

        if arrLen == 1:
            return nums[0]

        for i in range(arrLen):
            if(i == 0):
                if(nums[i] != nums[i+1]):
                    return nums[i]
            elif(i == arrLen - 1):
                if(nums[arrLen - 1] != nums[arrLen -2]):
                    return nums[arrLen - 1]
            else:
                if(nums[i] != nums[i-1] and nums[i] != nums[i+1]):
                    return nums[i]
        return -1