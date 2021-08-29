def findTriplet(a1, a2, a3,
                n1, n2, n3, sum):
 
    for i in range(0 , n1):
        for j in range(0 , n2):
            for k in range(0 , n3):
                if (a1[i] + a2[j] +
                    a3[k] == sum):
                    return True
 
    return False
 
# Driver Code
a1 = [ 1 , 2 , 3 , 4 , 5 ]
a2 = [ 2 , 3 , 6 , 1 , 2 ]
a3 = [ 3 , 2 , 4 , 5 , 6 ]
sum = 9
n1 = len(a1)
n2 = len(a2)
n3 = len(a3)
print("Yes") if findTriplet(a1, a2, a3,
                            n1, n2, n3,
                            sum) else print("No")