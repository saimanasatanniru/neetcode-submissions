class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set1 = set()
        left = 0
        right = 0
        longest = 0
        while right < len(s):
            while s[right] in set1:
                set1.remove(s[left])
                left += 1
            set1.add(s[right])
            longest = max(longest, len(s[left : right + 1]))
            right += 1
        return longest
        