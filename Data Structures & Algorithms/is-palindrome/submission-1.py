class Solution:
    def isPalindrome(self, s: str) -> bool:
        nn = ''
        ww = ''
        qq = ''
        for char in s:
            if char.isalnum():
                nn += char.lower()
            else:
                ww += char
        for c in s:
            if c.isalnum():
                qq += c.lower()
        return qq == nn[::-1]
