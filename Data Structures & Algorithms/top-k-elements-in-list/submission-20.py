
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}

        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        bucket = {}

        for key, value in dict1.items():
            if value not in bucket:
                bucket[value] = []
            bucket[value].append(key)

        res = []

        for i in range(max(dict1.values()), 0, -1):
            if i in bucket:
                for num in bucket[i]:
                    res.append(num)

                    if len(res) == k:
                        return res
