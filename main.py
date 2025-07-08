class Solution:
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

    def int_to_roman(self, num: int) -> str:
        val_to_roman = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        result = ""
        for value, symbol in val_to_roman:
            while num >= value:
                result += symbol
                num -= value
        return result

solution = Solution()
into_romans = solution.int_to_roman(int(input('Введите натуральное число для преобразования в римское:')))
print(into_romans)
into_integers = solution.roman_to_int(input('Введите число римскими цифрами для преобразования в натуральное:'))
print(into_integers)
