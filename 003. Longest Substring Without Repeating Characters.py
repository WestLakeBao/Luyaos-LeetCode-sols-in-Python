def lengthOfLongestSubstring(self, s):
    left = 0
    length = 0
    map = {}
    for right in range(len(s)):
        if s[right] in map:
            left = max(left, map[
                s[right]] + 1)  # consider the second 'a' in this string 'abcba', then max(left, map['a']+1) = left
        map[s[right]] = right
        length = max(length, right - left + 1)
    return length