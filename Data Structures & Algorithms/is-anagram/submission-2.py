class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ns = ''.join(sorted(s))
        nt = ''.join(sorted(t))
        if ns != nt:
            return False
        else:
            return True
        
        