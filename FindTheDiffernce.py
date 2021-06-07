s="abcd"
t="abcde"
for x,y in zip(s,t):
    print(ord(x)^ord(y))
