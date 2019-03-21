# Find the k nearest points from origin

# Input:
points = [[1,2], [2,3], [1,-1], [1,3],[1,1]]
k = 3

# Algorithm:
from heapq import heappop as pop, heappush as push

def kNearestPoints(points, k):
    heap = []; result = []
    for i in range(len(points)):
        x,y = points[i]
        dist = x*x + y*y
        push(heap, (dist, points[i]))
    for j in range(k):
        result.append(pop(heap)[1])
    return result

print(kNearestPoints(points, k))
