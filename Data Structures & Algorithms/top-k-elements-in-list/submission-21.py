class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            dict1[n] = 1 + dict1.get(n, 0)

        for n, c in dict1.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res