#valid palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True

        # s = [c.lower() for c in s if c.isalnum()]
        # return all(s[i]==s[~i] for i in range(len(s)//2))