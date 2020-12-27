# Given two strings s and t , write a function to determine if t is an anagram of s.

class Solution(object):
    def isAnagram(self, s, t):
        dict_s = {}
        for i in s:
            dict_s[i] = dict_s.get(i, 0) + 1
        dict_t = {}
        for j in t:
            dict_t[j] = dict_t.get(j, 0) + 1
        return dict_s == dict_t