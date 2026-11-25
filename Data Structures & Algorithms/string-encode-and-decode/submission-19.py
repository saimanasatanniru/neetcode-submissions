class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s += str(len(i)) + '#' + i
        return s

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            number = int(s[i : j])
            res.append(s[j + 1 : j + 1 + number])
            i = j + 1 + number
        return res