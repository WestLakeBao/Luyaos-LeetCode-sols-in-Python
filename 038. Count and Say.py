# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221


class Solution(object):
    def countAndSay(self, n):
        def count(s):
            i = 0
            count = 0
            say = ''
            for j in range(len(s)):
                if s[i] != s[j]:
                    say += str(count) + s[i]
                    i = j
                    count = 1
                else:
                    count += 1

            say += str(count) + s[i] #string variable is not callable
            return say

        num = '1'
        while n > 1:
            num = count(num)
            n -= 1
        return num

if __name__ == '__main__':
    print(Solution().countAndSay(5))