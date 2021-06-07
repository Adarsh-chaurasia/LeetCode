
s="1101010"
count_one=0
ones=0
count_zer=0
zeros=0
for each in s:
    if each=="1":
        count_one+=1
        if ones<count_one:
            ones=count_one
            count_zero=0
    
    else:
        count_zero+=1
        if zeros<count_zero:
            zeros=count_zero
            count_one=0
print(ones)
print(zeros)
