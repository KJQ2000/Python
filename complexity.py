#Part A
def local_peak(lst):
    for i in range(0,len(lst)):
        while lst[i] >lst[i]-1:
            while lst[i]>lst[i+1]:
                return i
            break
        continue
    i+=1
print (local_peak ([0,2,4,6,5,2]))
print(local_peak([8.8,8.6,8.1,8.2,8.1,8.01]))
print(local_peak([-7,-6,-2,-10,-5,-11]))

#Part B
def power(n,p):
    if p == 0 :
        return 1
    
    add = n
    result = n
    for i in range (1,p):
        for j in range (1,n):
            add = add + result
        result = add
    return result
print(power(2,8))
print(power(3,4))
