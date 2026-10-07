class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):

            # No new interval comes before current interval
            # No more merging needed -> add it and the rest 
            if newInterval[1] < intervals[i][0]: 
                res.append(newInterval)
                return res + intervals[i:]

            # Current interval comes before new interval
            # No overlap -> add current interval as is 
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])

            # Intervals overlap -> merge them
            # Expand newInterval to cover both ranges 
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        # If newInterval was not inserted earlier, add it to the end
        res.append(newInterval)

        return res


