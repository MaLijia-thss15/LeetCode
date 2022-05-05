class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1,
                "V": 5, "IV": 4,
                "X": 10, "IX": 9,
                "L": 50, "XL": 40,
                "C": 100, "XC": 90,
                "D": 500, "CD": 400,
                "M": 1000, "CM": 900,
                }
        l = len(s)
        num = 0
        i = 0
        while True:
            if i >= l:
                break
            if l - i >= 2:
                current_two_alphas = s[i] + s[i + 1]
                if current_two_alphas in dict:
                    num = num + dict[current_two_alphas]
                    i = i + 2
                    continue
            current_alpha = s[i]
            num = num + dict[current_alpha]
            i = i + 1
        return num


if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt(s="III"))
    print(s.romanToInt(s="LVIII"))
    print(s.romanToInt(s="MCMXCIV"))
