# Find the length of the longest substring T of a given string
# (consists of lowercase letters only) such that every character in T appears no less than k times.

class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k: return 0
        dict = {}
        for i in s:
            dict[i] = dict.get(i, 0)+1
        dict_sorted = sorted(dict.items(), key=lambda x: x[1])
        for i, count in dict_sorted:
            if count < k:
                s = s.replace(i, '-')
        if '-' not in s:
            return len(s)
        substrings = list(set(s.split('-')))
        result = 0
        for substring in substrings:
            result = max(result, self.longestSubstring(substring, k))
        return result