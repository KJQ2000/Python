##clubs_list = [(1,"C"),(2,"C"),(3,"C"),(4,"C"),(5,"C"),(6,"C"),(7,"C"),(8,"C"),(9,"C"),(10,"C"),(11,"C"),(12,"C"),(13,"C")]
##diamond_list =[(1,"D"),(2,"D"),(3,"D"),(4,"D"),(5,"D"),(6,"D"),(7,"D"),(8,"D"),(9,"D"),(10,"D"),(11,"D"),(12,"D"),(13,"D")]
##heart_list =[(1,"H"),(2,"H"),(3,"H"),(4,"H"),(5,"H"),(6,"H"),(7,"H"),(8,"H"),(9,"H"),(10,"H"),(11,"H"),(12,"H"),(13,"H")]
##spade_list = [(1,"S"),(2,"S"),(3,"S"),(4,"S"),(5,"S"),(6,"S"),(7,"S"),(8,"S"),(9,"S"),(10,"S"),(11,"S"),(12,"S"),(13,"S")]
##Part A
def suits(hand):
    for j in range (0, len(hand)):
        if "C"  == hand[j][1]:
            a.append(hand[j])
    j +=1
    for j in range (0, len(hand)):
        if "D" == hand[j][1]:
            b.append(hand[j])
    j +=1
    for j in range (0, len(hand)):
        if "H" == hand[j][1]:
            c.append(hand[j])
    j +=1
    for j in range (0, len(hand)):
        if "S" == hand[j][1]:
           d.append(hand[j])
    j +=1
    return [a] + [b] + [c] + [d]

a = []
b = []
c = []
d = []
print(suits([(4,"C"),(8,"H"),(3,"C"),(2,"D"),(8,"C")]))

#Part B
def flush(hand):
    for i in range (0,len(hand)):
        if hand[i][1] == hand[i+1][1]:
            i += 1
            return True
        return False
print(flush([(4,"D"),(8,"D"),(3,"D"),(2,"D"),(10,"D")]))


#Part C
def straight(hand):
    lst = ()
    lst1 = ()
    finalLst = []
    for i in hand:
        lst = list(hand)
        Lst1 = list(lst1)
        Lst1.append(min(hand))
        hand.remove(min(hand))
    while len(hand) > 0:
        Lst1.append(min(hand))
        hand.remove(min(hand))
    for j in range(1,len(Lst1)):
        while Lst1[j-1][0] + 1 != Lst1[j][0]:
            return False
    return True
print(straight([(3,"C"),(5,"D"),(4,"S"),(6,"H"),(2,"D")]))
print(straight([(12,"C"),(13,"D"),(11,"D")]))
print(straight([(2,"C"),(3,"D"),(4,"S"),(5,"H"),(7,"D")]))
print(straight([(2,"C"),(3,"D"),(4,"S"),(5,"H"),(5,"D")]))
print(straight([(4,"C"),(2,"D"),(5,"S"),(6,"H"),(3,"D")]))
