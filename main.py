class Solution(object):
    def roman_to_int(self, s: str) -> int:
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        n = len(s)
        for i in range(n):
            value = roman_to_int[s[i]]
            if i < n - 1 and value < roman_to_int[s[i + 1]]:
                result -= value
            else:
                result += value
        return result