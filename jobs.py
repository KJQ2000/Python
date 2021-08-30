    ##Part A
def max_sales(street):
    a = []
    if len(street)==1:
        return street[0]
    
    for j in range(len(street)):
        for i in range(len(street)):
            if street[0] == max(street):
                a.append(street[0])
                street[0] = 0
                street[1] = 0
                break
            if street[-1] == max(street):
                a.append(street[-1])
                street[-2] = 0
                street[-1] = 0
                break
            while street[i] == max(street):
                 a.append(street[i])
                 street[i-1] = 0
                 street[i] = 0
                 street[i+1] = 0
                 break
    return sum(a)
##print(max_sales([2,3,10,5,6,0,4,12,6]))
##print(max_sales([1,2]))
        

##Part B
def is_burger(breads):
    open_bread = ["ob","ow","or"]
    close_bread = ["cb","cw","cr"]

    stack = []

    if len(breads) %2 != 0:
        return False

    for b in breads:
        if b in open_bread:
            stack.append(b)
        elif b in close_bread:
            pos = close_bread.index(b)

            if ((len(stack)>0) and
                (open_bread[pos] == stack[len(stack) -1])):
                    stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    
##print(is_burger(["ob"]))
##print(is_burger(["ob","cb"]))
##print(is_burger(["ob","or","cb",]))
##print(is_burger(["ob","or","cr","cb"]))
##print(is_burger(["ob","or","cb","cr"]))
##print(is_burger(["ob","or","cr","ob","cb","cb"]))
##print(is_burger(["or","cr","ob","cb"]))
