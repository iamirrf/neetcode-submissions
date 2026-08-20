class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each number
        intcount = {}
        for num in nums:
            intcount[num] = intcount.get(num, 0) + 1
            
        # Step 2: Group numbers by their frequency (Bucket Sort)
        freq = [[] for _ in range(len(nums) + 1)]
        for number, count in intcount.items():
            freq[count].append(number)
            
        # Step 3: Collect the top k elements starting from the highest frequency
        result = []
        for count in range(len(nums), 0, -1):
            for number in freq[count]:
                result.append(number)
                if len(result) == k:
                    return result