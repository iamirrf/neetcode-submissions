class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        lists = {}
        listt = {}
        for i in range(len(s)):
            if s[i] in lists:
                lists[s[i]] += 1
            else:
                lists[s[i]] = 1
        for j in range(len(t)):
            if t[j] in listt:
                listt[t[j]] += 1
            else:
                listt[t[j]] = 1

        if lists == listt:
            return True
        else:
            return False

        