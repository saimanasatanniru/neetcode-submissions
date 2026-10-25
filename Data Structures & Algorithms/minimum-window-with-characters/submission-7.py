class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        required = len(need)
        min_len = float('inf')
        left = 0
        have = 0
        window = {}
        res = ""
        for right in range(len(s)):
            window[s[right]] = window.get(s[right] , 0) + 1
            if s[right] in need and window[s[right]] == need[s[right]]:
                have += 1

            while have == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left : right + 1]

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1

        return res
        