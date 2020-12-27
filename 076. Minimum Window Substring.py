# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

class Solution(object):
    def minWindow(self, s, t):
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        minLength = len(s) + 1
        left = 0
        match = set()
        s_dict = {}
        for right, char in enumerate(s):
            s_dict[char] = s_dict.get(char, 0) + 1
            if char in t_dict and t_dict[char] <= s_dict[char]:
                match.add(char)
                while len(match) == len(t_dict):
                    s_dict[s[left]] -= 1
                    if s[left] in t_dict and t_dict[s[left]] > s_dict[s[left]]:
                        match.remove(s[left])
                        if minLength > right - left + 1:
                            start = left
                            end = right
                            minLength = right - left + 1
                    left += 1
        if minLength == len(s)+1:
            return ''
        return s[start:end+1]

if __name__ == '__main__':
    print(Solution().minWindow(s="ADOBECODEBANC", t="ABC"))  # 'BANC'
    print(Solution().minWindow(s="aa", t="aa"))  # 'aa'

    print(Solution().minWindow(s='ABBCZBAC', t='ABC'))
    print(Solution().minWindow(s='ABCCBA', t='ABC'))
    print(Solution().minWindow(s='PQACBA', t='ABC'))
    print(Solution().minWindow(s='ABC', t='ABC'))