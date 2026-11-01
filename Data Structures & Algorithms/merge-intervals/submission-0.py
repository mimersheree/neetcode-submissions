class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(nlogn) time 

        # Sort by start time
        intervals.sort(key = lambda i : i[0])

        # Start with first interval 
        output = [intervals[0]]

        # End of last merged interval
        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            # If overlap, merge intervals
            # No overlap, add new interval 
            if start <= lastEnd: 
                output[-1][1] = max(lastEnd, end)
            else: 
                output.append([start, end])
        
        return output 