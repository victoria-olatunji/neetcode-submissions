class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        pref = strs[0]

        for word in strs[1:]:
            while not word.startswith(pref):
                pref = pref[:-1]

                if not pref:
                    return ""

        return pref
            
        
           
