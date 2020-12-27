# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

class Solution(object):
    def mySqrt(self, x):
        left, right = 0, x
        while left < right:
            mid = (left + right) // 2
            if x < mid * mid:
                right = mid
            else:
                left = mid + 1
        return left - 1 if left > 1 else left

if __name__ == '__main__':
    print(Solution().mySqrt(4))  # 2
    print(Solution().mySqrt(8))  # 2
    print(Solution().mySqrt(1))  # 1
