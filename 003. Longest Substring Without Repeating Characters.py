 # Given a string, find the length of the longest substring without repeating characters.

 # Input: "abcabcbb"
 # Output: 3
 # Explanation: The answer is "abc", with the length of 3.

 # Input: "bbbbb"
 # Output: 1
 # Explanation: The answer is "b", with the length of 1.

 # Input: "pwwkew"
 # Output: 3
 # Explanation: The answer is "wke", with the length of 3.
 #              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

 # time:
 # space:

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        length = 0
        map = {}
        for right in range(len(s)):
            if s[right] in map:
                left = max(left, map[s[right]] + 1)  # consider the second 'a' in this string 'abcba', then max(left, map['a']+1) = left
            map[s[right]] = right
            length = max(length, right - left + 1)
        return length

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
    print(Solution().lengthOfLongestSubstring("bbbbb")) # 1
    print(Solution().lengthOfLongestSubstring("pwwkew")) # 3