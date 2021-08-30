"""
Author: Kuan Jun Qiang
"""
#Q1
def num_rad_sort(nums, b):
    """
    Input:
        nums: an unsorted list of non negative integers
        b: an integer that >= 2
    Output:
        return a list of integer which contains exactly same elements as nums, and sorted in ascending order
    Time Complexity:
        O(n)+ O(b+n+b)*O(logb M) ≈ O((n + b) ∗ logbM)
        where n is length of nums, b is base and M is numerical value of the maximum element
    """
    max_item = nums[0]
    exp = 1
    col = 0
    #transverse through nums to find the largerst integer
    for item in nums:
        if item>max_item:
            max_item = item
    #check the times need for the sort
    while max_item//exp > 0:
    #build a count_array of a length of base +1(start from 0)
        count_array = [0]*(b+1)
    #putting a list into each space of count array so that it can be used to store multiple elements
        for i in range(0,len(count_array)):
            count_array[i] = []
    #count the value in the base given form
        for item in range(0,len(nums)):
            ans_base = (((nums[item])//(b**col))%b)
            count_array[ans_base].append(nums[item])
        nums = []#clear out the nums
        for i in range(0,len(count_array)):
            nums.extend(count_array[i])# insert back element in nums in  ascending order of specific row
        col+=1#so that col can tranverse to new row for sorting
        if col > 1:
            exp*=10
    return nums

nums = [43, 101, 22, 27, 5, 50, 15]
# print(num_rad_sort(nums, 4))

#Q2
import time
import random
import matplotlib.pyplot as plt

def base_timer(num_list,base_list):
    """
    use to record the time taken of the num_list sorted by num_rad_sort using integer in base_list as base accordingly
    Input:
        num_list: a list of non negative integer
        base_list: a listof integer with value >=2, sorted ascending
    
    Output:
        a list of number, element i in the list is the time taken for radix sort in Q1
    
    Time Complexity:
        O(b) where b is the length of base_list
    """
    ans = []
    for i in base_list:
        start = time.time()# record start time
        num_rad_sort(num_list, i)#perform radix sort
        end = time.time()#record end time
        ans.append(end - start)#calculate time taken for radix sort
    return ans
    


random.seed("FIT2004S22021")
data1 = [random.randint(0,2**25) for _ in range(2**15)]
data2 = [random.randint(0,2**25) for _ in range(2**16)]
bases1 = [2**i for i in range(1,23)]
bases2 = [2*10**6 + (5*10**5)*i for i in range(1,10)]
y1 = base_timer(data1, bases1)
y2 = base_timer(data2, bases1)
y3 = base_timer(data1, bases2)
y4 = base_timer(data2, bases2)

plt.xscale("log")
plt.plot(bases1,y1)
plt.plot(bases1,y2)
plt.show()

plt.xscale("linear")
plt.plot(bases2,y3)
plt.plot(bases2,y4)
plt.show()


#Q3

data = [("nuka", ["birds", "napping"]),
("hadley", ["napping birds", "nash equilibria"]),
("yaffe", ["rainy evenings", "the colour red", "birds"]),
("laurie", ["napping", "birds"]),
("kamalani", ["birds", "rainy evenings", "the colour red"])]

def interest_groups(data):
    """
    Input:
        data: a list of each element is a 2-element tuple, first element represent name and second represend interests
    Output:
        returns a list which each group represent people who have exactly same interest
    
    Time Complexity:
        O(N*M) where N is len(data) and M is the maximum nunmber of character all sets of interests
    """
    length_list = []
    interest_list = []
    compare_list = []
    output_list = []
    # seperate interest into characters and append into compare_list for comparasion
    for i in data:
        for j in i[1]:
            for character in j:
                interest_list.append(character)#represent M of each N
        compare_list.append(interest_list)#every N's M are append to compare_list
        interest_list = []#clear up interest list for next N
    #add length into length_list(count_array), which also indicate the number of sets will be return for this function
    for i in range(0,(len(compare_list))):
        if len(compare_list[i]) not in length_list:
            length_list.append(len(compare_list[i]))
    #if having same length of interest append into output_list
    for i in length_list:
        lst = []
        for j in range(0, len(compare_list)):
            if len(compare_list[j]) == i:
                lst.append(data[j][0])
        output_list.append(lst)
    return output_list

# print(interest_groups(data))