class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wd = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            wd[sorted_word].append(word)
        return list(wd.values())