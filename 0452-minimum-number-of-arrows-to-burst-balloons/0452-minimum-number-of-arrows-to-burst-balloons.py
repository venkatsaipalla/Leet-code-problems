class Solution(object):
    def findMinArrowShots(self, segments):
        ans, arrow = 0, 0
        for [start, end] in reversed(sorted(segments)):
            if ans == 0 or end < arrow:
                ans, arrow = ans + 1, start
        return ans