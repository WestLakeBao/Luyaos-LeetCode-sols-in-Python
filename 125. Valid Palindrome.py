# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

class Solution(object):
    def isPalindrome(self, s):
        s_str = ""
        for i in s:
            if i.isalnum():
                s_str += i

        return s_str.lower() == s_str[::-1].lower()

if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))