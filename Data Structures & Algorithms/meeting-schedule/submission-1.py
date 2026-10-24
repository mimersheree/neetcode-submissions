"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort meetings by their start time 
        intervals.sort(key = lambda i : i.start)

        # Compare each meeting with the one immediately before it  
        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            # If the current meeting starts before the previous one ends
            # the meetings overlap
            if i1.end > i2.start:
                return False
        
        # No overlaps found, then meetings can be attended 
        return True 