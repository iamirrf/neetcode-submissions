class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        amirset = set()
        for num in nums:
            if num in amirset:
                return True
            amirset.add(num)
        return False

         