import heapq

intervals=[[7,10],[2,4]]
intervals.sort()
minheap=[]
heapq.heappush(minheap,intervals[0][1])

for i in range(1,len(intervals)):
    if intervals[i][0]>=minheap[0]:
        heapq.heappop(minheap)
    heapq.heappush(minheap,intervals[i][1])
    

    
print(len(minheap))
