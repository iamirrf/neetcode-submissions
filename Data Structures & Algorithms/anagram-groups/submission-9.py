class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for i in range(len(strs)):
            key = ''.join(sorted(strs[i]))
            if key in group:
                group[key].append(strs[i])
            else:
                group[key] = [strs[i]]
        return list(group.values())
