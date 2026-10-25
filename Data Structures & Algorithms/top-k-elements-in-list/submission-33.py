class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]

        dict1 = {}
        for i in nums:
            dict1[i] = dict1.get(i, 0) + 1

        for key, value in dict1.items():
            freq[value].append(key)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
        