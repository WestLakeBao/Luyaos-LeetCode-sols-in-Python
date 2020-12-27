# Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

class Solution(object):
    def plusOne(self, digits):
        i = len(digits) - 1
        while (i >= 0):
            if digits[i] + 1 <= 9:
                digits[i] += 1
                return digits
            elif i == 0:
                if (digits[i] + 1) > 9:
                    digits[i] = 0
                    result = [1]
                    # result.append(digits)
                    return result + digits
            else:
                digits[i] = 0
                i -= 1


if __name__ == '__main__':
    print(Solution().plusOne([1, 2, 3]))