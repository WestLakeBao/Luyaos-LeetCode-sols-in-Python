# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# s = "leetcode"
# return 0.
#
# s = "loveleetcode"
# return 2.

import collections
import sys

class Solution(object):
    def firstUniqChar(self, s):
        count = collections.Counter(s)
        minIndex = sys.maxsize
        for letter, count in count.items():
            if count == 1:
                minIndex = min(minIndex, s.index(letter))
        if minIndex == sys.maxsize:
            return -1
        else:
            return minIndex

if __name__ == '__main__':
    print(Solution().firstUniqChar("leetcode"))  # 0
    print(Solution().firstUniqChar("loveleetcode"))  # 2