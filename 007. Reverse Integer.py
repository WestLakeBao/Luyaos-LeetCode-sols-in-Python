# Given a 32-bit signed integer, reverse digits of an integer.

class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        sign = int(x / abs(x))
        x *= sign
        result = 0
        while x:
            result = 10 * result + x % 10
            x //= 10
        if result > 2 ** 31 - 1:
            return 0
        else:
            return sign * result

if __name__ == '__main__':
    print(Solution().reverse(120))
    print(Solution().reverse(0))
    print(Solution().reverse(1534236469))
    print(Solution().reverse(123))
    print(Solution().reverse(1534236469))