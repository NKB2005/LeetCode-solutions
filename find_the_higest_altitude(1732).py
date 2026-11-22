class Solution(object):
    def largestAltitude(self, gain):
        curr_apt = 0
        highest_apt = 0
        for gains in gain:
            curr_apt = curr_apt + gains
            if curr_apt > highest_apt:
                highest_apt = curr_apt
        return highest_apt
        