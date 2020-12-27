# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        # solution 1: sliding window
        left = 0
        right = len(needle)
        while right <= len(haystack):
            if haystack[left:right] == needle:
                return left
            else:
                left += 1
                right += 1
        return -1

if __name__ == '__main__':
    print(Solution().strStr(haystack="hello", needle="ll"))  # 2
    print(Solution().strStr(haystack="aaaaa", needle="bba"))  # -1
    print(Solution().strStr(haystack="aaa", needle="aaaa"))  # -1
    print(Solution().strStr("mississippi", "issip"))  # 4