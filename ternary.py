lst1 = [1]
lst2 = [3,2,2,5,6,3,1,3]
lst3 = [1,2,3]

def ternary_partition(lst):
    i = 1
    swap_pos =1
    pivot = lst[0]

    if len(lst) ==1:
        return(0,1)

    while i < len(lst):
        if lst[i]<pivot:
            lst[i],lst[swap_pos] = lst[swap_pos],lst[i]
            swap_pos +=1
        if lst[i] == pivot:
            lst[i],lst[swap_pos+1] = lst[swap_pos+1],lst[i]
        i += 1
    lst[0],lst[swap_pos-1] = lst[swap_pos-1], lst[0]

    for i in lst:
        if lst[i]>pivot:
            return (swap_pos-1,i)
print (ternary_partition(lst2))
print(ternary_partition(lst1))
print(ternary_partition(lst3))
