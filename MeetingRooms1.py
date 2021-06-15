intervals=[[7,10],[2,4]]
intervals.sort()
attend=True
for i in range(len(intervals)-1):
    start=intervals[i][0]
    end=intervals[i][1]
    if end>intervals[i+1][1]:
        attend=False


print(attend)
