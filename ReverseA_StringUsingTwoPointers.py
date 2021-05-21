s=  ["H","a","n","n","a","h"]
temp=""
left=0
right=len(s)-1
while(left<right):
    temp=s[right]
    s[right]=s[left]
    s[left]=temp
    left+=1
    right-=1

print(s)
