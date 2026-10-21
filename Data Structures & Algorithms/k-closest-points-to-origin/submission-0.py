class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        # Calculate squared distance for each point and store it with its coordinates
        for x,y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])

        # Convert the list into a min-heap with the closest point at the top
        heapq.heapify(minHeap)
        res = []

        # Extract the k points with the smallest squared distances
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res