# Given an array of strings, group anagrams together.

class Solution(object):
    # Solution 1: categorize by sorted string
    # time: O(NKlogK) = O(N) for iterating * O(KlogK) for sorting each string, where N = len(strs), K=maximum length of a string in strs
    # space: O(NK)
    def groupAnagrams1(self, strs):
        map = {}
        for str in strs:
            map[tuple(sorted(str))] = map.get(tuple(sorted(str)), []) + [str]
        return [item for item in map.values()]

    # Solution 2: categorize by count
    # time: O(NK)
    # space: O(NK)
    def groupAnagrams(self, strs):
        map = {}
        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            map[tuple(count)] = map.get(tuple(count), []) + [str]
        return [item for item in map.values()]

if __name__ == '__main__':
    print(Solution().groupAnagrams(
        ["eat", "tea", "tan", "ate", "nat", "bat"]))  # [['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat']]