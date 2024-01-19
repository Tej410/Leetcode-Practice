class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        result = []
        sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        # sorted_freq_dict = dict(sorted_freq)
        for i in range(k):
            # a = list(sorted_freq_dict.keys())[len(freq)-1-i]
            a = sorted_freq[i][0]
            result.append(a)
        return result