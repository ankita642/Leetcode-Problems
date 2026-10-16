class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        n = len(s)
        i = 0
        j = n - 1

        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

