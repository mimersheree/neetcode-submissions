class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Map each number to its frequency
        freq = [[] for i in range(len(nums) + 1)] # Index = frequency, value = number with frequency 


        # Count how many times each number appears 
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Group numbers into buckets based on their frequency
        for n, c in count.items():
            freq[c].append(n)

        res = []

        # Traverse buckets from highest frequency to lowest
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n) # Add number to result 

                # Stop once we have the most k frequent numbers 
                if len(res) == k:
                    return res