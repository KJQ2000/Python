import copy

def subgrid_values(grid, r, c):
    val = []
    #get dimension of inner box
    n = int(len(grid)**(0.5))
    #get starting row and starting col
    row = (r//n)*n
    col = (c//n)*n
    for i in range(row, row+n):
        for j in range(col, col+n):
            val.append(grid[i][j])
    return val


##Part A
def grid_from_file(file_name):
    f = open(file_name)
    r = f.readlines()
    lst = []
    lst1 = []
    a = []
    real_lst = []
    num = ["1","2","3","4","5","6","7","8","9","0"]
    for i in range(len(r)):
        for j in range(len(r[i])):
            if r[i][j] == "/n":
                break
            if r[i][j] != ",":
                lst.append(r[i][j])
            pass
    for p in range(len(lst)):
        p = 0
        while len(lst) != 1:
            
            while lst[p] == "\n":
                lst1.append(lst[p])
                lst1.remove("\n")
                lst.pop(0)
                if len(lst)!= 1:
                    p = 0
                else:
                    exit
            lst1.append(lst[p])
            lst.pop(0)
            p = 0
        break
    d = (len(lst1))**0.5
    z = int(d)
    org_lst = len(lst1)
    integerz = int(org_lst)
    for k in range(0,z):
        c = 0
        for b in range(c+0,c+(org_lst//z)):
            if lst1[0] in num :
                lst1[0] = int(lst1[0])
                a.append(lst1[0])
                lst1.pop(0)
            else:
                a.append(lst1[0])
                lst1.pop(0)
        c += 1        
        real_lst.append(a)
        a = []
    return real_lst

##print(grid_from_file("daroufo.txt"))
##print(grid_from_file("gridB.txt"))

##Part B
def valid_entry(grid, num, r, c):
    if num in grid[r]:
        return False
    for i in range(len(grid)):
        if num == grid[i][c]:
            return False
    if num not in subgrid_values(grid,r,c) and grid[r][c] == "x":
        return True
    return False

full_grid = [ [2,"x","x","x"],["x",3,2,4],["x","x",4,2],[1,2,3,"x"] ]
grid = [ [1,"x","x","x"],["x","x","x","x"],["x","x",1,"x"],["x","x","x","x"] ]
##print(valid_entry(full_grid,1,0,3))

##print(valid_entry(grid,1,0,3))

##print(valid_entry(grid,1,1,2))

##print(valid_entry(grid,1,3,3))



##Part C
def grids_augmented_in_row(grid,num,r):
    lst = []
    for i in range(len(grid)):
        if grid[r][i] == num:
            return [grid]
        else:
            newgrid = copy.deepcopy(grid)
            if valid_entry(newgrid, num, r, i):
                newgrid[r][i] = num
                lst.append(newgrid)
    return lst

lite_grid = [ [1,"x","x","x"],["x","x","x","x"],["x","x","x","x"],["x",2,"x","x"] ]
full_grid = [ [2,"x","x","x"],["x",3,2,4],["x","x",4,2],[1,2,3,"x"] ]
grid_A = [ ["x","x",1,"x"],[4,"x","x","x"],["x","x","x",2],["x",3,"x","x"] ]

##print(grids_augmented_in_row(lite_grid,1,0))
##print(grids_augmented_in_row(lite_grid,1,1))
##print(grids_augmented_in_row(full_grid,1,1))
##print(grids_augmented_in_row(grid_A,1,2))

##Part D
def grids_augmented_with_number(grid,num):
    i = 0
    lst = [grid]

    while i < len(grid) and len(lst) > 0:
        lst1 = []
        for gri in lst:
            lst1 += grids_augmented_in_row(gri,num, i)
        lst = lst1
        i+=1
    return lst

##Part E
def solve_sudoku(file_name):
    f = []
    f += grid_from_file(file_name)
    final_result = [f]

    for num in range(1,len(grid)+1):
        result = []
        for i in final_result:
            result += grids_augmented_with_number(i,num)
        final_result = result
    return final_result

##print(solve_sudoku("gridA.txt"))
print(solve_sudoku("gridB.txt"))
