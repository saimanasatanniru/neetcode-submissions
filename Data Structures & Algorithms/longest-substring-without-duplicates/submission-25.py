class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        set1 = set()
        while right < len(s):
            while s[right] in set1:
                set1.remove(s[left])
                left += 1
            longest = max(longest, right - left + 1)
            set1.add(s[right])
            right += 1
        return longest

        