class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        count = 0
        for i in s:
            if i != ' ':
                count += 1
            elif i == ' ':
                count = 0

        return count