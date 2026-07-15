class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = []
        for i in range(len(nums)):
            if nums[i] in list:
                return True
            else:
                list.append(nums[i])
        return False