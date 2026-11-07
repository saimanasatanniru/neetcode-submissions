class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                pos1 = i + j
                pos2 = i + j + 1
                total = int(num1[i]) * int(num2[j]) + result[pos2]
                result[pos2] = total % 10
                result[pos1] += total // 10
        return "".join(map(str, result)).lstrip('0')
        