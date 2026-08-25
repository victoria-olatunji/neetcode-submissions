class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = Counter(s)
        nt = Counter(t)
        if ns == nt :
            return True
        else:
            return False
