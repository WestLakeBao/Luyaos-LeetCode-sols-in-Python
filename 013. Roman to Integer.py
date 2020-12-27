# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution(object):
    def romanToInt(self, s):
        result = 0
        previous_letter = None
        for letter in s:
            if letter == 'I':
                result += 1
            elif letter == 'V':
                result += 5
                if previous_letter == 'I':
                    result -= 2
            elif letter == 'X':
                result += 10
                if previous_letter == 'I':
                    result -= 2
            elif letter == 'L':
                result += 50
                if previous_letter == 'X':
                    result -= 20
            elif letter == 'C':
                result += 100
                if previous_letter == 'X':
                    result -= 20
            elif letter == 'D':
                result += 500
                if previous_letter == 'C':
                    result -= 200
            elif letter == 'M':
                result += 1000
                if previous_letter == 'C':
                    result -= 200
            previous_letter = letter
        return result

if __name__ == '__main__':
    print(Solution().romanToInt("III"))
    print(Solution().romanToInt("IV"))
    print(Solution().romanToInt("IX"))
    print(Solution().romanToInt("LVIII"))
    print(Solution().romanToInt("MCMXCIV"))