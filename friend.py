#Part A
def popular(graph_list,n):
    tpl = []
    for i in range(len(graph_list)):
        if len(graph_list[i]) >= n:
            tpl.append(i)
    return tpl
graph_list = [ [1,2,3], [0,3], [0,4], [0,1], [2] ]
n = 0
print(popular(graph_list,2))

#Part B
def foaf(graph_matrix,person1,person2):
    if graph_matrix[person1][person2] == 1 and graph_matrix[person1][person2] ==1:
        return False
    else:
        for i in range (len(graph_matrix)):
            if graph_matrix[i][person2] == 1 and graph_matrix[person1][i] ==1:
                return True
        if i ==len(clayton_matrix)-1:
            return False
clayton_matrix = [ [0,1,1,1,0],
[1,0,0,1,0],
[1,0,0,0,1],
[1,1,0,0,0],
[0,0,1,0,0] ]
print (foaf(clayton_matrix,0,4))
print(foaf(clayton_matrix,0,3))

# Part C
def society(graph_matrix,person):
    lst = []
    for i in range(len(graph_matrix[person])):
        if graph_matrix[person][i] ==1:
            lst.append(i)
    if len(lst)< 2:
        return False
    for j in range (len(lst)):
        for k in range (len(lst)-1):
            if graph_matrix[lst[j]][lst[k+1]] == 1:
                return True
                break
            elif j == (len(lst)-1):
                return False
graph_matrix = [ [0,1,1,1,0],
[1,0,0,1,0],
[1,0,0,0,1],
[1,1,0,0,0],
[0,0,1,0,0] ]
print(society(graph_matrix,0))
