A = [1,2,3,4]
B = [2,3,4,5,6]

for i in A:
    for j in B:
        if i< j:
            print('({},{})'.format(i,j))
            
# The time complexity of this code is O(mn)*, where m and n are the lengths of lists A and B, respectively. This is because for each element in A, we're iterating over all elements in B.