class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        for char in list(s):
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1   
        for char in list(t):
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1   
        if s_dict == t_dict:
            return True
        return False


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = list(s)
        second = list(t)
        first.sort()
        second.sort()
        if first == second:
            return True
        return False