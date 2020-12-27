# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".

class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        common = ""

        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                if i > len(strs[j]) - 1 or strs[0][i] != strs[j][i]:
                    return common
            common += strs[0][i]
        return common


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
    print(Solution().longestCommonPrefix(["a"]))
    print(Solution().longestCommonPrefix(["aa", "a"]))