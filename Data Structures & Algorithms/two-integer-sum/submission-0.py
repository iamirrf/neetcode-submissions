class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in complement:
                return [complement[num], i]
            else:
                complement[nums[i]] = i






        